# from django.contrib.auth.models import User

from account.models import ResetPasswordNumberModel

list = ResetPasswordNumberModel.objects.all()
for item in list:
    print(item)


# user = User.objects.get(username="a1@gmail.com")
# print(user.id)
