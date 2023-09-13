from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from account.models import AccountModel


class AccountCreationForm(UserCreationForm):
    class Meta:
        model = AccountModel
        fields = ("email",)


class AccountChangeForm(UserChangeForm):
    class Meta:
        model = AccountModel
        fields = ("email",)
