from rest_framework import serializers

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
