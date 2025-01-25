import json 

from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from engage.request.api.v1.serializers import RespondCreateSerializer, RespondListSerializer
from engage.request.models import Request
from engage.utils.local_govt_utils import find_local_govt


class RespondAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        local_govt_id = find_local_govt(request)
        responds = Request.objects.all()
        if local_govt_id:
            responds = responds.filter(localgovt__id=local_govt_id)
        serializer = RespondListSerializer(responds, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        local_govt_id = find_local_govt(request)
        if local_govt_id:
            if not request.body:
                return Response(
                    {
                        "success":False,
                        "message": "Full fill the required fields",
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
            
            data = json.loads(request.body)
            data['localgovt'] = local_govt_id
            serializer = RespondCreateSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        "success": True,
                        "message": "Respond created successfully",
                        "data":serializer.data,
                    },
                    status=status.HTTP_201_CREATED
                )
    
        return Response(
            {
                "success": False,
                "message": "Respond not created",
            },
            status=status.HTTP_400_BAD_REQUEST,
        )
    
    def patch(self, request):
        return Response(status=status.HTTP_200_OK)
