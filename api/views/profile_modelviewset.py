from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from api.models import ProfileModel
from api.serializers import ProfileSerializer


class ProfileModelViewSet(ModelViewSet):
    queryset = ProfileModel.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [
        IsAuthenticated,
    ]
