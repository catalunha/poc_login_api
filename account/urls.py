from rest_framework.routers import SimpleRouter
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from account.views import (
    AccountCreateAPIView,
    AccountMeAPIView,
    AccountNewPasswordAPIView,
    AccountResetPasswordAPIView,
    ProfileModelViewSet,
)

simpleRouter = SimpleRouter()
simpleRouter.register(
    "account/profile", ProfileModelViewSet, basename="profile_account"
)

urlpatterns = [
    path("account/create/", AccountCreateAPIView.as_view(), name="user_create"),
    path("account/me/", AccountMeAPIView.as_view(), name="user_me"),
    path(
        "account/resetpassword/",
        AccountResetPasswordAPIView.as_view(),
        name="user_register",
    ),
    path(
        "account/newpassword/",
        AccountNewPasswordAPIView.as_view(),
        name="user_register",
    ),
    path("account/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("account/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("account/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("", include(simpleRouter.urls)),
]
