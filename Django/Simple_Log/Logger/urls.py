from django.urls import path
from .views import *

app_name = 'Logger'
urlpatterns = [
    path('page1/', view1),
    path('page2/', view2),
]