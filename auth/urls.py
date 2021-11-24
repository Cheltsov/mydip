from django.urls import path
from . import views

app_name = "auth"
urlpatterns = [
    path('', views.auth, name='auth'),
    path('sing-in', views.singIn, name='singIn'),
    path('logout', views.logOut, name='logOut'),
]