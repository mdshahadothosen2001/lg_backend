from rest_framework import serializers
from engage.request.models import Request


class RespondListSerializer(serializers.ModelSerializer):
    responder_picture = serializers.SerializerMethodField()
    responder_name = serializers.SerializerMethodField()
    responder_id = serializers.SerializerMethodField()
    member_name = serializers.SerializerMethodField()
    member_picture = serializers.SerializerMethodField()
    member_id = serializers.SerializerMethodField()
    localgovt = serializers.SerializerMethodField()

    class Meta:
        model = Request
        fields = [
            'responder_name',
            'responder_picture',
            'responder_id',
            'member_name',
            'member_picture',
            'member_id',
            "localgovt",
            'title',
            'description',
            'file',
            'status',
            'possibility_amount',
            'possibility_time_required',
        ]

    def get_responder_name(self, obj):
        return f"{obj.requested_citizen.first_name} {obj.requested_citizen.last_name}"
    
    def get_responder_picture(self, obj):
        return f"{obj.requested_citizen.picture} {obj.requested_citizen.picture}"
    
    def get_responder_id(self, obj):
        return f"{obj.requested_citizen.id}"
    
    def get_member_name(self, obj):
        return f"{obj.taken_member.first_name} {obj.taken_member.last_name}" if obj.taken_member else None
    
    def get_member_picture(self, obj):
        return f"{obj.taken_member.picture}" if obj.taken_member else None
    
    def get_member_id(self, obj):
        return f"{obj.taken_member.id}" if obj.taken_member else None
    
    def get_localgovt(self, obj):
        return f"{obj.localgovt.division} {obj.localgovt.district} {obj.localgovt.upazila} {obj.localgovt.union}"


class RespondCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = [
            'requested_citizen',
            'localgovt',
            'taken_member',
            'title',
            'description',
            'file',
            'status',
            'possibility_amount',
            'possibility_time_required',
        ]
