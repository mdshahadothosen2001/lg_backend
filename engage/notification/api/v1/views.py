from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from engage.notification.api.v1.serializers import NoticeSerializer, EvenSerializer
from engage.notification.models import Notice, Event


class NoticeListView(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request):
        union = request.query_params.get('union_id')
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
        union = request.query_params.get('union_id')
        member_id = request.query_params.get('member_id')
        if union:
            events = Event.objects.filter(is_active=True, union__id=union)
            if member_id:
                events = events.filter(members__regex=fr'(^|,){member_id}(,|$)')
            serializer = EvenSerializer(events, many=True)

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
