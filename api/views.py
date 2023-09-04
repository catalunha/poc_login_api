# type: ignore
from rest_framework import viewsets
from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from rest_framework import status
from .serializers import ProfileSerializer, UsersSerializer
from .models import ProfileModel
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
# from .permissions import IsQwner


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
    permission_classes = [IsAuthenticated, ]
    http_method_names = ['get', 'patch', 'post', 'delete', 'options', 'head', ]

    def list(self, request, *args, **kwargs):

        print('ProfileViewSet.list')
        print('request.user=', request.user)
        print('self.request.user=', self.request.user)
        print('isAuthenticated=', request.user.is_authenticated)
        return super().list(request, *args, **kwargs)

    def get_queryset(self):
        qs = super().get_queryset()
        print('ProfileViewSet params')
        print(self.kwargs)
        print(self.request.query_params)
        user_id = self.request.query_params.get('user_id', None)
        if user_id is not None:
            qs = qs.filter(user_id=user_id)
        return qs


class UsersViewSet(viewsets.ModelViewSet):
    serializer_class = UsersSerializer
    permission_classes = [IsAuthenticated, ]
    http_method_names = ['get', 'patch', 'post', 'delete', 'options', 'head', ]

    def get_queryset(self):
        # print(self.request.user.__dict__)  # type: ignore
        print(self.request.user.id)  # type: ignore
        User = get_user_model()
        qs = User.objects.filter(id=self.request.user.id)  # type: ignore

        return qs

    def get_permissions(self):
        if self.request.method == 'POST':
            return []
        return super().get_permissions()

    @action(methods=['get'], detail=False)
    def me(self, request, *arg, **kwargs):
        obj = self.get_queryset().first()
        serializer = self.get_serializer(instance=obj)
        return Response(serializer.data)
