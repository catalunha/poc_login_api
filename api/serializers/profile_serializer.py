from rest_framework import serializers
from api.models import ProfileModel


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
