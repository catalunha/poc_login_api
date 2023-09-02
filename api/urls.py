from rest_framework.routers import SimpleRouter
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from .views import ProfileViewSet, data, data_pk


simpleRouter = SimpleRouter()
simpleRouter.register('profile', ProfileViewSet, basename='profile-api')

urlpatterns = [
    path('profile/data/', data, name='data'),
    path('profile/data/<int:pk>/', data_pk, name='data_pk'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('', include(simpleRouter.urls)),
]
