import random
from django.db import models


def create_number():
    number = "".join(random.choice("1234567890") for _ in range(6))
    return number


class ResetPasswordNumberModel(models.Model):
    username = models.EmailField()
    number = models.CharField(max_length=6, default=create_number, blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self) -> str:
        return f"id:{self.id}, username:{self.username}, number:{self.number}, created:{self.created}"
