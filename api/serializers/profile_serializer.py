from rest_framework import serializers
from api.models import ProfileModel


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = [
            "id",
            "user",
            "nickname",
            "name",
            "photo",
            "phone",
        ]
