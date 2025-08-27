from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from engage.utils.jwt_token import generate_jwt
from engage.accounts.models import User


class LoginView(APIView):
    def post(self, request):
        nid = request.data.get("nid")

        is_user = User.objects.filter(nid_no=nid).exists()

        if not is_user:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

        token = generate_jwt(nid)
        return Response({"token": token, "nid": nid})
