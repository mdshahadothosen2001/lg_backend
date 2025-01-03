from rest_framework.serializers import ModelSerializer

from engage.service.models import ServiceType, Service


class ServiceTypeSerializer(ModelSerializer):
    class Meta:
        model = ServiceType
        fields = [
            'id', 
            'name',
        ]


class ServiceSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = [
            'id', 
            'title',
            'service_type',
            'icon',
            'link',
        ]
