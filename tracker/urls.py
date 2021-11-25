from django.urls import path
from . import views

app_name = "tracker"
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('settings', views.settings, name='settings'),
    path('settings-ext', views.settingsExt, name='settingsExt'),
    path('settings-ext/create', views.settingsExtCreate, name='settingsExtCreate'),
    path('settings-ext/edit/<int:id>', views.settingsExtEdit, name='settingsExtEdit'),
    path('settings-ext/delete/<int:id>', views.settingsExtDelete, name='settingsExtDelete'),
]
