# type: ignore
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.views import APIView

# from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from api.serializers import UserNewPasswordSerializer, ProfileSerializer
from api.models import ResetPasswordNumberModel, ProfileModel


class UserNewPasswordAPIView(APIView):
    def post(self, request):
        print("UserResetPassword.post")
        print(request.data)
        userNewPasswordSerializer = UserNewPasswordSerializer(data=request.data)
        if userNewPasswordSerializer.is_valid(raise_exception=True):
            print("Dados válidos")
            resetPasswordNumberModel = get_object_or_404(
                ResetPasswordNumberModel.objects.all(),
                username=request.data["username"],
                number=request.data["number"],
            )
            print(resetPasswordNumberModel)
            user = User.objects.get(pk=resetPasswordNumberModel.user.id)
            user.set_password(request.data["password"])
            user.save()
            resetPasswordNumberModel.delete()
        return Response({}, status=status.HTTP_404_NOT_FOUND)


class ProfileViewSet(ModelViewSet):
    queryset = ProfileModel.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [
        IsAuthenticated,
    ]
