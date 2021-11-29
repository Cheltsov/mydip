from django.contrib import admin
from core.models import User, UserExtSettings, BodyWorkout, UserFood


class UserAdmin(admin.ModelAdmin):
    pass


class UserExtSettingsAdmin(admin.ModelAdmin):
    pass


class BodyWorkoutAdmin(admin.ModelAdmin):
    pass


class UserFoodAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, UserAdmin)
admin.site.register(UserExtSettings, UserExtSettingsAdmin)
admin.site.register(BodyWorkout, BodyWorkoutAdmin)
admin.site.register(UserFood, UserFoodAdmin)
