# serializers.py
from rest_framework import serializers
from .models import Service

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'union', 'title', 'description', 'link', 'is_active']
        # যদি সব ফিল্ড দিতে চাও তাহলে fields = "__all__"
