from rest_framework.serializers import ModelSerializer

from engage.notification.models import Notice, Event


class NoticeSerializer(ModelSerializer):
    class Meta:
        model = Notice
        fields = [
            'id', 
            'title',
            'date',
            'file',
        ]


class EvenSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = [
            'id', 
            'title',
            'description',
            'start',
            'duration',
            'link',
        ]
