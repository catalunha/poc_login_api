from api.models import ResetPasswordNumberModel

list = ResetPasswordNumberModel.objects.all()
print(list)
# num = ResetPasswordNumberModel.objects.get(pk=1)
# num.attempt = 0
# num.save()
