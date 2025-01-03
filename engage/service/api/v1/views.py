from django.shortcuts import get_list_or_404

from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from engage.service.api.v1.serializers import ServiceTypeSerializer, ServiceSerializer
from engage.service.models import ServiceType, Service


class ServiceTypeListView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ServiceTypeSerializer
    queryset = ServiceType.objects.all()


class ServiceListView(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request):
        localgovt_id = request.query_params.get('localgovt_id')
        service_type_id = request.query_params.get('service_type_id')

        if localgovt_id:
            if service_type_id:
                services = get_list_or_404(Service, localgovt__id=localgovt_id, service_type__id=service_type_id)
            else:
                services = get_list_or_404(Service, localgovt__id=localgovt_id)
            serializer = ServiceSerializer(services, many=True)

            data = {
                "success": True,
                "message": "Service list retrieved successfully.",
                "data": serializer.data
            }
            return Response(data)
        if service_type_id:
            services = get_list_or_404(Service, localgovt__id=None, service_type__id=service_type_id)
        else:
            services = get_list_or_404(Service, localgovt__id=None)
        serializer = ServiceSerializer(services, many=True)

        data = {
            "success": True,
            "message": "Service list retrieved successfully.",
            "data": serializer.data
        }
        return Response(data)
