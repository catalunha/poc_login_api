# type: ignore
from rest_framework.views import APIView
from rest_framework import viewsets

from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# from rest_framework import status
from .serializers import ProfileSerializer, UsersSerializer, UserCreateSerializer
from .models import ProfileModel
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = ProfileModel.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [
        IsAuthenticated,
    ]


class UserCreateAPIView(APIView):
    def post(self, request):
        print("UserCreateAPIView.post")

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


class UsersViewSet(viewsets.ModelViewSet):
    serializer_class = UsersSerializer
    permission_classes = [
        IsAuthenticated,
    ]
    http_method_names = [
        "get",
        "patch",
        "options",
        "head",
    ]

    def get_queryset(self):
        # print(self.request.user.__dict__)  # type: ignore
        print(self.request.user.id)  # type: ignore
        User = get_user_model()
        qs = User.objects.filter(id=self.request.user.id)  # type: ignore
        return qs

    @action(methods=["get"], detail=False)
    def me(self, request, *arg, **kwargs):
        obj = self.get_queryset().first()
        serializer = self.get_serializer(obj)
        return Response(serializer.data)
