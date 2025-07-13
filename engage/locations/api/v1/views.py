import json 

from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from engage.locations.api.v1.serializers import DivisionCreateSerializer, DistrictCreateSerializer, UpazilaCreateSerializer, UnionCreateSerializer
from engage.locations.models import Division, District, Upazila, Union


class DivisionListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        divisions = Division.objects.all()
        serializer = DivisionCreateSerializer(divisions, many=True)

        data = {
            "success": True,
            "message": "Division list retrieved successfully.",
            "data": serializer.data
        }
        return Response(data)
    

class DistrictListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        division_id = request.query_params.get('division_id')
        if division_id:
            districts = District.objects.filter(division__id=division_id)
            serializer = DistrictCreateSerializer(districts, many=True)

            data = {
                "success": True,
                "message": "District list retrieved successfully.",
                "data": serializer.data
            }
            return Response(data)
        
        data = {
                "success": False,
                "message": "District list can't retrieved successfully.",
                "data": []
            }
        return Response(data, status=status.HTTP_400_BAD_REQUEST)
    

class UpazilaListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        district_id = request.query_params.get('district_id')
        if district_id:
            upazilas = Upazila.objects.filter(district__id=district_id)
            serializer = UpazilaCreateSerializer(upazilas, many=True)

            data = {
                "success": True,
                "message": "Upazila list retrieved successfully.",
                "data": serializer.data
            }
            return Response(data)
        
        data = {
                "success": False,
                "message": "Upazila list can't retrieved successfully.",
                "data": []
            }
        return Response(data, status=status.HTTP_400_BAD_REQUEST)


class UnionListView(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request):
        upazila_id = request.query_params.get('upazila_id')
        if upazila_id:
            unions = Union.objects.filter(upazila__id=upazila_id)
            serializer = UnionCreateSerializer(unions, many=True)

            data = {
                "success": True,
                "message": "Union list retrieved successfully.",
                "data": serializer.data
            }
            return Response(data)
        
        data = {
                "success": False,
                "message": "Union list can't retrieved successfully.",
                "data": []
            }
        return Response(data, status=status.HTTP_400_BAD_REQUEST)
