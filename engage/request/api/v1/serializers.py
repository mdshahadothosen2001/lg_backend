from rest_framework import serializers
from engage.request.models import Request


class RespondListSerializer(serializers.ModelSerializer):
    responder_picture = serializers.SerializerMethodField()
    responder_name = serializers.SerializerMethodField()
    responder_id = serializers.SerializerMethodField()
    responder_email = serializers.SerializerMethodField()
    member_name = serializers.SerializerMethodField()
    member_picture = serializers.SerializerMethodField()
    member_id = serializers.SerializerMethodField()
    member_email = serializers.SerializerMethodField()
    union_id = serializers.SerializerMethodField()
    union_name = serializers.SerializerMethodField()

    class Meta:
        model = Request
        fields = [
            'id',
            'responder_name',
            'responder_picture',
            'responder_id',
            'responder_email',
            'member_name',
            'member_picture',
            'member_id',
            'member_email',
            'union',
            'union_id',
            'union_name',
            'title',
            'description',
            'file',
            'status',
            'possibility_amount',
            'possibility_time_required',
        ]

    def get_responder_name(self, obj):
        return obj.requested_citizen.name if obj.requested_citizen and obj.requested_citizen else None
    
    def get_responder_picture(self, obj):
        return f"{obj.requested_citizen.picture} {obj.requested_citizen.picture}"
    
    def get_responder_id(self, obj):
        return f"{obj.requested_citizen.id}"
    
    def get_responder_email(self, obj):
        return f"{obj.requested_citizen.email}" if obj.requested_citizen else None
    
    def get_member_name(self, obj):
        return obj.taken_member.user.name if obj.taken_member else None
    
    def get_member_picture(self, obj):
        return f"{obj.taken_member.user.picture}" if obj.taken_member else None
    
    def get_member_id(self, obj):
        return f"{obj.taken_member.user.id}" if obj.taken_member else None
    
    def get_member_email(self, obj):
        return f"{obj.taken_member.user.email}" if obj.taken_member else None
    
    def get_union_id(self, obj):
        return f"{obj.union.id}" if obj.union else None
    
    def get_union_name(self, obj):
        return f"{obj.union.name}" if obj.union else None


class RespondCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = [
            'requested_citizen',
            'taken_member',
            'title',
            'union',
            'description',
            'file',
            'status',
            'possibility_amount',
            'possibility_time_required',
        ]
