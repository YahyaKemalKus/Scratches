from django.contrib import admin
from django.urls import path,include
from chat.views import chat

urlpatterns = [
    path('admin1/', admin.site.urls),
    path('chat/', include('chat.urls')),
    path('', include('customauth.urls')),
]
