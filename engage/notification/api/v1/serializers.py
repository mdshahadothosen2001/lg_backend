from rest_framework.serializers import ModelSerializer

from engage.notification.models import Notice, Even


class NoticeSerializer(ModelSerializer):
    class Meta:
        model = Notice
        fields = [
            'id', 
            'title',
            'file',
        ]


class EvenSerializer(ModelSerializer):
    class Meta:
        model = Even
        fields = [
            'id', 
            'title',
            'start',
            'link',
        ]
