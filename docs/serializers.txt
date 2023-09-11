# type: ignore
from rest_framework import serializers
from .models import ProfileModel

from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator


class UserCreateSerializer(serializers.Serializer):
    username = serializers.EmailField(
        required=True,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
            ),
        ],
    )
    password = serializers.CharField(
        required=True,
        min_length=8,
    )

    def validate(self, data):
        if data["username"] == data["password"]:
            raise serializers.ValidationError("Username e email são iguais")
        return data


class UserNewPasswordSerializer(serializers.Serializer):
    username = serializers.EmailField(required=True)
    number = serializers.CharField(max_length=6, min_length=6, required=True)
    password = serializers.CharField(required=True, min_length=8)

    def validate(self, data):
        if data["username"] == data["password"]:
            raise serializers.ValidationError("Username e email não podem ser iguais")
        return data


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = [
            "id",
            "user",
            "username",
            "nickname",
            "name",
            "photo",
            "phone",
            "is_active",
        ]


# class RegisterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         # model = get_user_model()
#         fields = [
#             "username",
#             "password",
#         ]

#     def create(self, validated_data):
#         print("RegisterSerializer.create")
#         if self.is_valid(raise_exception=True):
#             user = User.objects.create_user(
#                 validated_data["username"],
#                 validated_data["username"],
#                 validated_data["password"],
#             )
#             user.save()
#         return user


# class UsersSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = get_user_model()
#         fields = [
#             "id",
#             "username",
#         ]


# from rest_framework import serializers
# from .models import ProfileModel
# from django.contrib.auth import get_user_model


# class ProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ProfileModel
#         fields = ['id', 'user_id', 'username', 'name', ]


# class UsersSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = get_user_model()
#         fields = ['id', 'username', ]
