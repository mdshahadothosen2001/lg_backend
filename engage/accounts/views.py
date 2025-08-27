from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from engage.utils.jwt_token import generate_jwt, decode_jwt
from engage.accounts.models import User


class LoginView(APIView):
    def post(self, request):
        nid = request.data.get("nid")

        is_user = User.objects.filter(nid_no=nid).exists()

        if not is_user:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

        token = generate_jwt(nid)
        return Response({"token": token, "nid": nid})


class ProfileView(APIView):
    def get(self, request):
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            return Response({"error": "Authorization header missing"}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            token = auth_header.split(" ")[1]
        except:
            return Response({"error": "Invalid Authorization header"}, status=status.HTTP_401_UNAUTHORIZED)


        payload = decode_jwt(token)
        nid = payload.get("nid")

        try:
            user = User.objects.get(nid_no=nid)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        return Response({
            "id": user.id,
            "nid": user.nid_no,
            "picture": user.picture,
            "name": f"{user.name}",
            "gender": user.gender,
            "email": user.email,
        })
