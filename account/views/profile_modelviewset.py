from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from account.models import ProfileModel
from account.serializers import ProfileSerializer


class ProfileModelViewSet(ModelViewSet):
    queryset = ProfileModel.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [
        IsAuthenticated,
    ]
