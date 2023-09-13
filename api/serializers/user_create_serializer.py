from django.contrib.auth import get_user_model
from rest_framework import serializers

from rest_framework.validators import UniqueValidator


class UserCreateSerializer(serializers.Serializer):
    email = serializers.EmailField(
        required=True,
        validators=[
            UniqueValidator(
                queryset=get_user_model().objects.all(),
            ),
        ],
    )
    password = serializers.CharField(
        required=True,
        min_length=8,
    )

    def validate(self, data):
        if data["email"] == data["password"]:
            raise serializers.ValidationError("email e password não pode ser iguais")
        return data
