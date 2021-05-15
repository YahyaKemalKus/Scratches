from django.shortcuts import render,HttpResponse,redirect,reverse
from .decorators import *
from .models import Usr,Sessions
from datetime import datetime,timedelta
from django.core.signing import Signer
from django.conf import settings

signer = Signer()
umng = Usr.manager
COOKIE_EXPR_TIME = settings.COOKIE_LIFE #minutes
COOKIE_LIFE = datetime.now()+timedelta(minutes=COOKIE_EXPR_TIME)

def index(request):
    return render(request,'customauth/index.html')

@no_session
def register(request):
    return render(request,'customauth/register.html')

@valid_session
def logout(request):
    session_key = Sessions.manager.key_from_request(request)
    session_data = Sessions.manager.data_from_request(request)
    username = session_data['username']
    Sessions.manager.delete_session(session_key)
    umng.change_activeness(username,0)
    return render(request,'customauth/logged_out.html',context=session_data)

@no_session
def registration(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        if 'admin' in request.POST.keys():
            new_user = Usr.manager.add_user(username=username,password=password,is_admin=True)
        else:
            new_user = Usr.manager.add_user(username=username,password=password,is_admin=False)
        if new_user:
            return redirect('customauth:registered_page',username=username)
        return redirect('customauth:register_page')
    else:
        return redirect('customauth:main_page')

@no_session
def registered(request,username):
    return render(request,'customauth/registered.html',context={'username':username})

@admin
def admin_page(request):
    session_data = Sessions.manager.data_from_request(request)
    return render(request,"customauth/admin.html",context=session_data)

@no_session
def login(request):
    return render(request,'customauth/login.html')

@no_session
def verify(request):                         #verifies username and password coming from login page.
    if request.method=='POST':               #if verification fails,redirects client to login page back.
        username=request.POST['username']    #if client tries to get this page from url,redirects client to main_page
        password=request.POST['password']
        is_verified = Usr.manager.verify_user(username=username,password=password)

        if is_verified:
            response = render(request,'customauth/authed.html',context={'username':username})
            session_data = signer.sign_object({'username':username})
            session_key = Sessions.manager.create_session(session_data, COOKIE_EXPR_TIME)
            response.set_cookie('session_key', session_key, httponly=True, expires=COOKIE_LIFE)
            umng.change_activeness(username,1)
            return response

        if not is_verified:
            return redirect('customauth:login_page')

    if request.method=='GET':
        return redirect('customauth:main_page')
