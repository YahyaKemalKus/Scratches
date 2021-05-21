from django.db.models import Manager
import argon2
from random import choice
from django.db import IntegrityError
from datetime import datetime,timedelta,timezone
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings

Hasher = argon2.PasswordHasher(hash_len=32,salt_len=16) #using argon2 algorithm to protect passwords.
cookie_life = settings.COOKIE_LIFE


class UserManager(Manager):
    def add_user(self,*,username,password,is_admin):             #adding password's argon2 hash to database.
        Hash = Hasher.hash(password)
        try:
            new_user = super().create(username = username,password = Hash,is_admin=is_admin)
            return new_user
        except IntegrityError:
            return False


    def verify_user(self,*,username,password):          #user verification.returns True/False.
        try:
            user = super().get(pk=username)
            verified = Hasher.verify(user.password,password)
            return verified
        except(self.model.DoesNotExist,argon2.exceptions.VerifyMismatchError):
            return False


    def is_admin(self,username):
        return super().get(pk=username).is_admin

    def change_activeness(self,username,value:bool):
        user = super().get(pk = username)
        user.is_active = value
        user.save()


class SessionManager(Manager):
    def create_session(self,session_data="", expr_minutes=cookie_life):
        """
        creates new session.

            Parameters:
                session_data(str):Information about session's capabilities or attributes.
                expr_minutes(int):how many minutes session will be valid.(expiration time)

            Returns:
                session_key(str):session key of created session.
        """
        char_list = [*range(65,90),*range(97,122)]
        key_length = 32
        session_key = "".join([chr(choice(char_list)) for r in range(key_length)])
        expiration = datetime.now(tz=timezone.utc)+timedelta(minutes=expr_minutes)
        try:
            super().create(session_key  = session_key,
                           session_data = session_data,
                           expiration   = expiration,
                           )
        except IntegrityError:                          #if created session key already exists,creates again.
            self.create_session(session_data)

        return session_key

    def delete_session(self,session_key):               #deletes given session key from database
        """
        deletes session.

            Parameters:
                session_key(str):session key to find will be deleted session.

            Returns:
                returns session_key if successfully deleted,False if session key doesn't exist.
        """
        session = self.exist(session_key)
        if session:
            session.delete()
            return session_key
        return False

    def exist(self, session_key):
        """
        Checks if given session key is in database.

            Parameters:
                session_key(str):session key to check if session is in database.

            Returns:
                returns Session model instance if session is in database,False if session doesn't exist.
        """
        try:
            session = super().get(session_key = session_key)
            return session
        except ObjectDoesNotExist:
            return False

    def check_exprdate(self, session_key): #to do
        """
        Checks expiration of session.

            Parameters:
                session_key(str):session key to check if session is expired.

            Returns:
                returns True if session is not expired,False if session is expired.
        """
        session = self.exist(session_key)
        if session:
            expr_date = session.expiration
            curr_time = datetime.now(tz=timezone.utc)
            if expr_date.timestamp() > curr_time.timestamp():
                return True

        return False

    def delete_if_expired(self,request):
        session_key = self.key_from_request(request)
        if session_key:
            if not self.check_exprdate(session_key):  #if not valid anymore
                from .models import Usr
                session_data = self.data_from_request(request)
                if session_data:
                    username = session_data['username']
                    Usr.manager.change_activeness(username, 0)
                self.delete_session(session_key)
                return True
        return False

    def refresh_expr(self,request,minutes = cookie_life):
        session_key = self.key_from_request(request)
        if session_key:
            try:
                session = super().get(session_key = session_key)
                session.expiration = datetime.now(tz=timezone.utc)+ timedelta(minutes=minutes)
                session.save()
            except ObjectDoesNotExist:
                pass
        return False

    def data_from_request(self,request):
        session_key = self.key_from_request(request)
        if session_key:
            try:
                data = super().get(session_key=session_key).data
                return data
            except ObjectDoesNotExist:
                return False
        return False

    def key_from_request(self,request):
        cookies = request.COOKIES
        if 'session_key' in request.COOKIES.keys():
            return cookies.get('session_key')
        else:
            return False

    def is_admin(self, session_key):
        from .models import Usr
        try:
            session_data = super().get(session_key=session_key).data
            username = session_data.get('username')
            return Usr.manager.is_admin(username)
        except ObjectDoesNotExist:
            return False

    def is_valid(self, request):
        session_key = self.key_from_request(request)
        if session_key:
            return self.exist(session_key)
        return False
