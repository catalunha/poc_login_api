# type: ignore
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from account.serializers import AccountCreateSerializer
from account.models import ProfileModel


class AccountCreateAPIView(APIView):
    def post(self, request):
        print("AccountCreateAPIView.post")
        print("request.data: ", request.data)

        accountCreateSerializer = AccountCreateSerializer(data=request.data)
        accountCreateSerializer.is_valid(raise_exception=True)

        email = request.data["email"]
        password = request.data["password"]

        # user = get_user_model()
        user = get_user_model().objects.create_user(email, password)
        user.save()

        self._createProfile(user)
        print("AccountCreateAPIView.post end")
        return Response({"user_id": user.id}, status=status.HTTP_200_OK)

    def _createProfile(self, user):
        ProfileModel.objects.create(
            user=user,
        )
