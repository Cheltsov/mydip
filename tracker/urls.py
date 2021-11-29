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
    path('goals', views.goal, name='goal'),
    path('goals-param/<int:id>', views.goal_param, name='goal_param'),
    path('goals-select/<int:id>', views.select_goal, name='select_goal'),
    path('goals_delete/<int:id>', views.delete_goal, name='delete_goal'),
    path('workout', views.workout_list, name='workout_list'),
    path('workout/show/<int:id>', views.workout_show, name='workout_show'),
    path('workout/stop/<int:id>', views.workout_stop, name='workout_stop'),
    path('workout/new/<int:id>', views.workout_new, name='workout_new'),

    path('food', views.foodIndex, name='foodIndex'),
    path('food/add', views.foodAdd, name='foodAdd'),
    path('food/update/<int:id>', views.foodUpdate, name='foodUpdate'),
    path('food/delete/<int:id>', views.foodDelete, name='foodDelete'),
    path('food/stat', views.foodStat, name='foodStat'),
]
