# type: ignore
from rest_framework import serializers


class UserNewPasswordSerializer(serializers.Serializer):
    username = serializers.EmailField(required=True)
    number = serializers.CharField(max_length=6, min_length=6, required=True)
    password = serializers.CharField(required=True, min_length=8)

    def validate(self, data):
        if data["username"] == data["password"]:
            raise serializers.ValidationError("Username e email não podem ser iguais")
        return data
