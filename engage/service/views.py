from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Service
from .serializers import ServiceSerializer

class ServiceListView(APIView):
    def get(self, request):
        # query param থেকে union_id নাও
        union_id = request.query_params.get("union_id")
        
        # filter only active services
        services = Service.objects.filter(is_active=True)
        
        # যদি union_id দেয়া থাকে তাহলে filter করো
        if union_id:
            services = services.filter(union__id=union_id)
        
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
