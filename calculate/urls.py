from django.urls import path
from . import views

app_name = "calculate"
urlpatterns = [
    path('calculate_harrison', views.calculate_harrison, name='calculate_harrison'),
    path('calculate_mifflin', views.calculate_mifflin, name='calculate_mifflin'),
    path('calculate_voz', views.calculate_voz, name='calculate_voz'),
]
