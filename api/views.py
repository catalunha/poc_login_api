from rest_framework import viewsets

from rest_framework.decorators import api_view
from rest_framework.response import Response
# from rest_framework import status
from .serializers import ProfileSerializer
from .models import ProfileModel


@api_view()
def data(request):
    a = ProfileModel.objects.all()

    return Response({"data": len(a)})


@api_view()
def data_pk(request, pk):
    a = ProfileModel.objects.all()

    return Response({"data_pk": len(a), "pk": pk, })


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = ProfileModel.objects.all()
    serializer_class = ProfileSerializer
