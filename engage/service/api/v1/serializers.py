from rest_framework.serializers import ModelSerializer

from engage.service.models import Service


class ServiceSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = [
            'id', 
            'title',
            'link',
        ]
