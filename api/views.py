from rest_framework.views import APIView
from rest_framework.response import Response


class Test1(APIView):
    def get(self, request):
        return Response({"ok": "..."})
