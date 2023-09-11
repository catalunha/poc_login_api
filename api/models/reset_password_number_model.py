import random
from django.db import models
from django.contrib.auth.models import User


def create_number():
    # print("".join(random.choice("1234567890") for _ in range(6)))
    number = "".join(random.choice("1234567890") for _ in range(6))
    return number


class ResetPasswordNumberModel(models.Model):
    user = models.OneToOneField(
        User,
        related_name="resetpasswordnumbers",
        related_query_name="resetpasswordnumber",
        on_delete=models.CASCADE,
    )
    username = models.EmailField()
    number = models.CharField(max_length=6, default=create_number, blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self) -> str:
        return f"{self.id}-{self.user.id}-{self.username}-{self.number}-{self.created}"
