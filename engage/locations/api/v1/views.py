import json 

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from engage.locations.api.v1.serializers import DivisionCreateSerializer, DistrictCreateSerializer, UpazilaCreateSerializer, UnionCreateSerializer
from engage.locations.models import Division, District, Upazila, Union


class DivisionCreateView(APIView):
    serializer_class = DivisionCreateSerializer

    def post(self, request):
        file_path = request.data.get('file_path')
        if not file_path:
            return Response('file_path path is required.')
        
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                file_data = json.load(file)
        except:
            return Response('bad request. {file_path}')
        division_data = []
        for item in file_data:
            fields = item.get('fields')
            name = fields[0].get('name')
            division_data.append(
                {
                    "id": item.get('pk'),
                    'name': name
                }
            )

        serializer = self.serializer_class(data=division_data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class DivisionListView(APIView):
    def get(self, request):
        divisions = Division.objects.all()
        serializer = DivisionCreateSerializer(divisions, many=True)

        data = {
            "success": True,
            "message": "Division list retrieved successfully.",
            "data": serializer.data
        }
        return Response(data)


class DistrictCreateView(APIView):
    serializer_class = DistrictCreateSerializer

    def post(self, request):
        file_path = request.data.get('file_path')
        if not file_path:
            return Response('file_path path is required.')
        
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                file_data = json.load(file)
        except:
            return Response('bad request. {file_path}')
        district_data = []
        for item in file_data:
            fields = item.get('fields')
            name = fields[0].get('name')
            district_data.append(
                {
                    "id": item.get('pk'),
                    'name': name,
                    'division': item.get('division_id')
                }
            )

        serializer = self.serializer_class(data=district_data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class DistrictListView(APIView):
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


class UpazilaCreateView(APIView):
    serializer_class = UpazilaCreateSerializer

    def post(self, request):
        file_path = request.data.get('file_path')
        if not file_path:
            return Response('file_path path is required.')
        
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                file_data = json.load(file)
        except:
            return Response('bad request. {file_path}')
        upazila_data = []
        for item in file_data:
            fields = item.get('fields')
            name = fields[0].get('name')
            upazila_data.append(
                {
                    "id": item.get('pk'),
                    'name': name,
                    'district': item.get('district_id')
                }
            )

        serializer = self.serializer_class(data=upazila_data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class UpazilaListView(APIView):
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


class UnionCreateView(APIView):
    serializer_class = UnionCreateSerializer

    def post(self, request):
        file_path = request.data.get('file_path')
        if not file_path:
            return Response('file_path path is required.')
        
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                file_data = json.load(file)
        except:
            return Response('bad request. {file_path}')
        union_data = []
        for item in file_data:
            fields = item.get('fields')
            name = fields[0].get('name')
            union_data.append(
                {
                    "id": item.get('pk'),
                    'name': name,
                    'upazila': item.get('upazila_id')
                }
            )

        serializer = self.serializer_class(data=union_data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class UnionListView(APIView):
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
