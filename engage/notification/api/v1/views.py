from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from engage.notification.api.v1.serializers import NoticeSerializer, EvenSerializer
from engage.notification.models import Notice, Event


class NoticeListView(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request):
        union = request.query_params.get('union')
        if union:
            notices = Notice.objects.filter(is_active=True, union__id=union)
            serializer = NoticeSerializer(notices, many=True)

            data = {
                "result": True,
                "data": serializer.data
            }
        else:
            data = {
                "result": True,
                "data": []
            }
        return Response(data)


class EvenListView(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request):
        union = request.query_params.get('union')
        if union:
            evens = Event.objects.filter(is_active=True, union__id=union)
            serializer = EvenSerializer(evens, many=True)

            data = {
                "result": True,
                "data": serializer.data
            }
        else:
            data = {
                "result": True,
                "data": []
            }
        return Response(data)
