from django.contrib import admin
from core.models import User, UserExtSettings


class UserAdmin(admin.ModelAdmin):
    pass


class UserExtSettingsAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, UserAdmin)
admin.site.register(UserExtSettings, UserExtSettingsAdmin)