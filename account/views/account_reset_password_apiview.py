# type: ignore
from django.contrib.auth import get_user_model

from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ParseError, Throttled

from account.models import ResetPasswordNumberModel
from account.exceptions import EmailServiceUnavaliable


class AccountResetPasswordAPIView(APIView):
    def post(self, request):
        print("AccountResetPasswordAPIView.post")
        print("request.data: ", request.data)

        if request.data.get("email") is None:
            raise ParseError("O campo email não foi informado")
        email = request.data["email"]
        user = get_object_or_404(
            get_user_model().objects.all(),
            email=email,
        )
        print("user.id", user.id)

        number = self._update_number(user.email)

        self._send_mail(user.email, number)

        return Response({"detail": "Enviamos um email com instruções"})

    def _update_number(self, email):
        updated = True
        if not updated:
            raise Throttled(wait=60 * 60)
        ResetPasswordNumberModel.objects.filter(email=email).delete()

        newResetPasswordNumberModel = ResetPasswordNumberModel.objects.create(
            email=email
        )
        return newResetPasswordNumberModel.number

    def _send_mail(self, email, number):
        print(f"Número: {number} enviado ao email: {email}")
        sent = True
        if not sent:
            raise EmailServiceUnavaliable()
