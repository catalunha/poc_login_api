from django.db import models
from django.contrib.auth.models import User


class ProfileModel(models.Model):
    user_id = models.OneToOneField(
        User, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

    # def __str__(self) -> str:
    #     return f'self.id
