from rest_framework.routers import SimpleRouter
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from .views import (
    UserCreateAPIView,
    UserMeAPIView,
    UserResetPassword,
    UserNewPassword,
    ProfileViewSet,
)


simpleRouter = SimpleRouter()
simpleRouter.register("profile", ProfileViewSet, basename="profile_api")

urlpatterns = [
    path("user/create/", UserCreateAPIView.as_view(), name="user_create"),
    path("user/me/", UserMeAPIView.as_view(), name="user_me"),
    path("user/resetpassword/", UserResetPassword.as_view(), name="user_register"),
    path("user/newpassword/", UserNewPassword.as_view(), name="user_register"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("", include(simpleRouter.urls)),
]
