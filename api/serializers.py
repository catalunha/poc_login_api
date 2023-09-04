# type: ignore
from rest_framework import serializers
from .models import ProfileModel
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ['id', 'user_id', 'username', 'name', ]


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # model = get_user_model()
        fields = ['id', 'username', 'password', ]

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'], validated_data['username'], validated_data['password'],)
        print('user antes save')
        user.save()
        print('user criado')
        return user


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', ]


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
