# type: ignore
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

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

        email = request.data["email"]
        number = request.data["number"]
        password = request.data["password"]

        resetPasswordNumberModel = get_object_or_404(
            ResetPasswordNumberModel.objects.all(),
            email=email,
            number=number,
        )
        print(resetPasswordNumberModel)

        user = get_user_model().objects.get(email=email)
        user.set_password(password)
        user.save()

        resetPasswordNumberModel.delete()

        return Response({"detail": "Senha alterada com sucesso"})
