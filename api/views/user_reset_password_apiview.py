# type: ignore
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ParseError, Throttled

from api.models import ResetPasswordNumberModel
from api.exceptions import EmailServiceUnavaliable


class UserResetPasswordAPIView(APIView):
    def post(self, request):
        print("UserResetPasswordAPIView.post")
        print("request.data: ", request.data)

        if request.data.get("username") is None:
            raise ParseError("O campo username não foi informado")
        user = get_object_or_404(
            User.objects.all(),
            username=request.data["username"],
        )
        print("user.id", user.id)

        number = self._update_number(user.username)

        self._send_mail(number)

        return Response({"detail": "Enviamos um email com instruções"})

    def _update_number(self, username):
        updated = True
        if not updated:
            raise Throttled(wait=60 * 60)
        ResetPasswordNumberModel.objects.filter(username=username).delete()

        newResetPasswordNumberModel = ResetPasswordNumberModel.objects.create(
            username=username
        )
        print("Número enviado ao email: ", newResetPasswordNumberModel.number)
        return newResetPasswordNumberModel.number

    def _send_mail(self, number):
        sent = True
        if not sent:
            raise EmailServiceUnavaliable()
