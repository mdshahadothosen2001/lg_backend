from rest_framework import serializers
from engage.local_govt.models import Member


class MemberSerializer(serializers.ModelSerializer):
    picture = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()

    class Meta:
        model = Member
        fields = [
            'name',
            'picture',
            'position',
            'start_at',
            'end_at',
        ]

    def get_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"
    
    def get_picture(self, obj):
        return f"{obj.user.picture} {obj.user.picture}"
