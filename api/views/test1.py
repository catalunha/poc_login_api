from rest_framework.views import APIView
from rest_framework.response import Response

# from rest_framework.exceptions import (
#     ParseError,
#     AuthenticationFailed,
#     NotAuthenticated,
#     PermissionDenied,
# )


class Test1(APIView):
    def get(self, request):
        # raise PermissionDenied()
        # raise NotAuthenticated()
        # {"detail": "Authentication credentials were not provided."}
        # raise AuthenticationFailed()
        # {"detail": "Incorrect authentication credentials."}
        # raise ParseError(detail="teste")
        # raise ParseError()
        # {"detail": "Malformed request."}
        return Response({"ok": "..."})
