# type: ignore

from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from api.serializers import ProfileSerializer


class UserMeAPIView(APIView):
    # authentication_classes = [authentication.]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        print("UserMeAPIView.get")

        user = self.request.user
        profile = user.profiles

        profileSerializer = ProfileSerializer(profile)

        return Response(
            {
                "user": {
                    "id": user.id,
                    "email": user.email,
                    "is_active": user.is_active,
                },
                "profile": profileSerializer.data,
            },
        )
