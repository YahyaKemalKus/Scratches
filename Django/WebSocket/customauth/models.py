from django.db.models import *
from .managers import UserManager,SessionManager
from datetime import datetime
from django.core.signing import Signer

signer = Signer()


class Usr(Model):
    username = CharField(max_length=16,
                          unique=True,
                          default="",
                          primary_key=True)

    password = CharField(max_length=256,null=True)
    is_active = BooleanField(default=False)
    is_admin = BooleanField(default=False)

    manager = UserManager()

    class Meta:
        db_table = "AAusers"

    def __str__(self):
        return self.username


class Sessions(Model):
    session_key = CharField(max_length=24,default="",primary_key=True)
    session_data = CharField(max_length=1024,default="")
    expiration = DateTimeField(default=datetime.now())

    manager = SessionManager()

    class Meta:
        db_table = "AAsessions"

    def __str__(self):
        return self.session_key

    @property
    def data(self):                             #returns decoded type of session_data
        decoded = signer.unsign_object(self.session_data)
        return decoded

    @data.setter
    def data(self,new_data:dict):               #model.data = {newdict}.avoid using it for stability.
        encoded = signer.sign_object(new_data)  #but if you want to use it.assign to a dict as same as {'username':name}
        self.session_data = encoded
        self.save()
