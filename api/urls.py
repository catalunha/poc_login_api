from django.urls import path

from api.views import Test1


urlpatterns = [
    path("test1/", Test1.as_view(), name="test1"),
]
