# type: ignore
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import (
    ProfileSerializer,
    UserCreateSerializer,
    UserNewPasswordSerializer,
)
from .models import ProfileModel, ResetPasswordNumberModel


class UserCreateAPIView(APIView):
    def post(self, request):
        print("UserCreateAPIView.post")
        print("request.data: ", request.data)
        userCreateSerializer = UserCreateSerializer(data=request.data)
        if userCreateSerializer.is_valid(raise_exception=True):
            print("dados válidos")
            username = request.data["username"]
            password = request.data["password"]

            user = User.objects.create_user(username, username, password)
            # user.is_active = False
            user.save()
            _createProfile(user)
            return Response({"user": user.id}, status=status.HTTP_200_OK)


def _createProfile(user):
    ProfileModel.objects.create(
        user=user,
        username=user.username,
    )


class UserMeAPIView(APIView):
    # como colocar a classe de authentication para jwt ?
    # authentication_classes = [authentication.]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        print("MeAPIView.get")
        # Qual a diferença aqui entre self.request e request ?
        print("self.request.user: ", self.request.user)
        print("request.user: ", request.user)
        print("request.auth: ", request.auth)
        print("request.data: ", request.data)
        print("request.authenticators: ", request.authenticators)
        user = self.request.user
        print(user)
        print("user.profiles: ", user.profiles)
        profile = user.profiles
        print(profile)
        profileSerializer = ProfileSerializer(profile)
        print(profileSerializer.data)

        return Response(
            {
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "is_active": user.is_active,
                },
                "profile": profileSerializer.data,
            },
        )


class UserResetPassword(APIView):
    def post(self, request):
        print("UserResetPassword.post")
        print("request.user: ", request.user)
        print("request.user.id: ", request.user.id)
        print("request.data: ", request.data)
        print("request.data.keys: ", request.data.keys())
        if request.data.get("username") is None:
            return Response(
                {"username": "Este campo não foi encontrado"},
                status=status.HTTP_404_NOT_FOUND,
            )
        user = get_object_or_404(
            User.objects.all(),
            username=request.data["username"],
        )
        print(user.id)
        # +++ delete old numbers
        resetPasswordNumberModel = ResetPasswordNumberModel.objects.filter(
            username=request.data["username"]
        )
        resetPasswordNumberModel.delete()
        newResetPasswordNumberModel = ResetPasswordNumberModel.objects.create(
            user=user,
            username=user.username,
        )
        print(newResetPasswordNumberModel.number)
        # --- delete old numbers
        # +++ analisar tempo de envio
        # hoje deleta o old number mas é necessario analisar melhor este contexto
        # print(resetPasswordNumberModel)
        # # print(len(resetPasswordNumberModel))
        # past = resetPasswordNumberModel.created.replace(tzinfo=None)
        # print("past: ", past)
        # now = datetime.datetime.now()
        # print("now: ", now)
        # dif = now - past
        # minutes = dif.total_seconds() / 60
        # print("dif: ", dif)
        # print("minutes: ", minutes)
        # --- analisar tempo de envio

        # +++ enviar email
        if not send_mail(newResetPasswordNumberModel.number):
            return Response(
                {"erro": "codigo nao enviado para email"},
                status=status.HTTP_412_PRECONDITION_FAILED,
            )
        # --- enviar email
        return Response()


def send_mail(number):
    return True


class UserNewPassword(APIView):
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
