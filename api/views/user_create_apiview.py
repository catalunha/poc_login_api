# type: ignore
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from api.serializers import UserCreateSerializer
from api.models import ProfileModel


class UserCreateAPIView(APIView):
    def post(self, request):
        print("UserCreateAPIView.post")
        print("request.data: ", request.data)
        userCreateSerializer = UserCreateSerializer(data=request.data)
        userCreateSerializer.is_valid(raise_exception=True)
        print("dados válidos")
        username = request.data["username"]
        password = request.data["password"]

        user = User.objects.create_user(username, username, password)
        user.save()
        self._createProfile(user)
        return Response({"user": user.id}, status=status.HTTP_200_OK)

    def _createProfile(user):
        ProfileModel.objects.create(
            user=user,
            username=user.username,
        )