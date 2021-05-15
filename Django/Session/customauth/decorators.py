from .models import Sessions
from django.shortcuts import redirect

mng = Sessions.manager

def valid_session(func):            #Decorator for checking session validation.(we can call it as login required)
    def validate(*args,**kwargs):   #If session is invalid,redirects to login page.
        request = args[0]
        is_valid = mng.is_valid(request)

        if is_valid:
            return func(*args,**kwargs)
        else:
            return redirect('customauth:login_page')
    return validate

def admin(func):                            #decorator for checking if existing session has admin power.
    @valid_session                          #session validation checking by 'valid_session' decorator first of all.
    def check_permission(*args,**kwargs):   #if session valid and has no admin power redirect to main page
        request=args[0]
        session_key = Sessions.manager.key_from_request(request)
        is_admin = Sessions.manager.is_admin(session_key)
        if is_admin:
            return func(*args,**kwargs)
        else:
            return redirect('customauth:main_page')
    return check_permission

def no_session(func):                        #this decorator only allows not logged in users to view page.
    def check(*args,**kwargs):    #for example login page or registration page.
        request = args[0]
        is_valid = mng.is_valid(request)

        if not is_valid:
            return func(*args, **kwargs)
        else:
            return redirect('customauth:main_page')

    return check
