from django.urls import path
from .views import *

app_name ='customauth'
urlpatterns = [
    path('',index,name="main_page"),
    path('login/',login,name="login_page"),
    path('verify/',verify,name="verify"),
    path('admin/',admin_page,name='admin_page'),
    path('register/',register,name='register_page'),
    path('registration/',registration,name='registration_page'),
    path('registered/<str:username>',registered,name='registered_page'),
    path('logout/',logout,name='logout_page'),
]