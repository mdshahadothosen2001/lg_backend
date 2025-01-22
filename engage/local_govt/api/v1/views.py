import json 

from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from engage.local_govt.api.v1.serializers import MemberSerializer
from engage.local_govt.models import Member


class MemberListAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        local_govt_id = request.GET.get('local_govt_id')
        members = Member.objects.all()
        if local_govt_id:
            members = members.filter(localgovt__id=local_govt_id)
        serializer = MemberSerializer(members, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
