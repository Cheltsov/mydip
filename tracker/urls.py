from django.urls import path
from . import views

app_name = "tracker"
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('settings', views.settings, name='settings'),
]
