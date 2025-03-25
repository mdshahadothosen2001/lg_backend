from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from engage.notification.api.v1.serializers import NoticeSerializer, EvenSerializer
from engage.notification.models import Notice, Event


class NoticeListView(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request):
        notices = Notice.objects.filter(is_active=True)
        serializer = NoticeSerializer(notices, many=True)

        data = {
            "result": True,
            "data": serializer.data
        }
        return Response(data)


class EvenListView(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request):
        evens = Event.objects.filter(is_active=True)
        serializer = EvenSerializer(evens, many=True)

        data = {
            "result": True,
            "data": serializer.data
        }
        return Response(data)
