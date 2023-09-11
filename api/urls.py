from rest_framework.routers import SimpleRouter
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from api.views import (
    UserCreateAPIView,
    UserMeAPIView,
    UserResetPasswordAPIView,
    UserNewPasswordAPIView,
    ProfileModelViewSet,
)


simpleRouter = SimpleRouter()
simpleRouter.register("profile", ProfileModelViewSet, basename="profile_api")

urlpatterns = [
    path("user/create/", UserCreateAPIView.as_view(), name="user_create"),
    path("user/me/", UserMeAPIView.as_view(), name="user_me"),
    path(
        "user/resetpassword/", UserResetPasswordAPIView.as_view(), name="user_register"
    ),
    path("user/newpassword/", UserNewPasswordAPIView.as_view(), name="user_register"),
    path("user/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("user/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("user/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("", include(simpleRouter.urls)),
]
