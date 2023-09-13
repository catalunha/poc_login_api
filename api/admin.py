from django.contrib import admin

from .models import ProfileModel


@admin.register(ProfileModel)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["id", "created", "updated", "user_id", "name"]
