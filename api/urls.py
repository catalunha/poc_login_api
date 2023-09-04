from rest_framework.routers import SimpleRouter
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from .views import ProfileViewSet, RegisterViewSet, UsersViewSet


simpleRouter = SimpleRouter()
simpleRouter.register('profile', ProfileViewSet, basename='profile-api')
simpleRouter.register('users', UsersViewSet, basename='users')

urlpatterns = [
    # path('profile/data/', data, name='data'),
    # path('profile/data/<int:pk>/', data_pk, name='data_pk'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('user/register/', RegisterViewSet.as_view(), name='user_register'),

    path('', include(simpleRouter.urls)),
]
