from rest_framework import serializers
from .models import ProfileModel
from django.contrib.auth import get_user_model


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ['id', 'user_id', 'username', 'name', ]


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', ]
