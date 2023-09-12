# type: ignore
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response

from api.models import ResetPasswordNumberModel
from api.serializers import UserNewPasswordSerializer


class UserNewPasswordAPIView(APIView):
    def post(self, request):
        print("UserNewPasswordAPIView.post")
        print(request.data)

        userNewPasswordSerializer = UserNewPasswordSerializer(data=request.data)
        userNewPasswordSerializer.is_valid(raise_exception=True)

        username = request.data["username"]
        number = request.data["number"]
        password = request.data["password"]

        resetPasswordNumberModel = get_object_or_404(
            ResetPasswordNumberModel.objects.all(),
            username=username,
            number=number,
        )
        print(resetPasswordNumberModel)

        user = User.objects.get(username=username)
        user.set_password(password)
        user.save()

        resetPasswordNumberModel.delete()

        return Response({"detail": "Senha alterada com sucesso"})
