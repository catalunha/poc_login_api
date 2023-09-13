from django.db import models
from django.conf import settings
from account.models import BaseModel


class ProfileModel(BaseModel):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name="profiles",
        related_query_name="profile",
        on_delete=models.CASCADE,
    )
    nickname = models.CharField(max_length=500, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    photo = models.CharField(max_length=500, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self) -> str:
        return f"ProfileModel {self.id}: {self.nickname}"
