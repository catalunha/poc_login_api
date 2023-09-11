# type: ignore
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.views import APIView

from rest_framework.response import Response

from api.models import ResetPasswordNumberModel


class UserResetPasswordAPIView(APIView):
    def post(self, request):
        print("UserResetPassword.post")
        print("request.user: ", request.user)
        print("request.user.id: ", request.user.id)
        print("request.data: ", request.data)
        print("request.data.keys: ", request.data.keys())
        if request.data.get("username") is None:
            return Response(
                {"username": "Este campo não foi encontrado"},
                status=status.HTTP_404_NOT_FOUND,
            )
        user = get_object_or_404(
            User.objects.all(),
            username=request.data["username"],
        )
        print(user.id)
        # +++ delete old numbers
        resetPasswordNumberModel = ResetPasswordNumberModel.objects.filter(
            username=request.data["username"]
        )
        resetPasswordNumberModel.delete()
        newResetPasswordNumberModel = ResetPasswordNumberModel.objects.create(
            user=user,
            username=user.username,
        )
        print(newResetPasswordNumberModel.number)
        # --- delete old numbers
        # +++ analisar tempo de envio
        # hoje deleta o old number mas é necessario analisar melhor este contexto
        # print(resetPasswordNumberModel)
        # # print(len(resetPasswordNumberModel))
        # past = resetPasswordNumberModel.created.replace(tzinfo=None)
        # print("past: ", past)
        # now = datetime.datetime.now()
        # print("now: ", now)
        # dif = now - past
        # minutes = dif.total_seconds() / 60
        # print("dif: ", dif)
        # print("minutes: ", minutes)
        # --- analisar tempo de envio

        # +++ enviar email
        if not self._send_mail(newResetPasswordNumberModel.number):
            return Response(
                {"erro": "codigo nao enviado para email"},
                status=status.HTTP_412_PRECONDITION_FAILED,
            )
        # --- enviar email
        return Response()

    def _send_mail(number):
        return True
