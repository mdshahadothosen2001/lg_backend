from rest_framework.serializers import ModelSerializer

from engage.locations.models import Division, District, Upazila, Union


class DivisionCreateSerializer(ModelSerializer):
    class Meta:
        model = Division
        fields = [
            'id', 
            'name',
        ]


class DistrictCreateSerializer(ModelSerializer):
    class Meta:
        model = District
        fields = [
            'id', 
            'name',
            'division',
        ]


class UpazilaCreateSerializer(ModelSerializer):
    class Meta:
        model = Upazila
        fields = [
            'id', 
            'name',
            'district',
        ]


class UnionCreateSerializer(ModelSerializer):
    class Meta:
        model = Union
        fields = [
            'id', 
            'name',
            'upazila',
        ]

