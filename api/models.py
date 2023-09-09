from django.db import models
from django.contrib.auth.models import User


class ProfileModel(models.Model):
    user = models.OneToOneField(
        User,
        related_name="users",
        related_query_name="user",
        on_delete=models.CASCADE,
    )
    username = models.CharField(max_length=50)
    nickname = models.CharField(max_length=500, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    photo = models.CharField(max_length=500, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    is_active = models.BooleanField(default=False, blank=True)

    def __str__(self) -> str:
        return f"{self.id}: {self.username}"
