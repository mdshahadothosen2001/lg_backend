from rest_framework import serializers
from engage.local_govt.models import Member, Contribution


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


class ContributionSerializer(serializers.ModelSerializer):
    contributors = serializers.SerializerMethodField()
    class Meta:
        model = Contribution
        fields = [
            'id',
            'project_title',
            'contributors',
            'localgovt',
            'areas',
            'start_at',
            'end_at',
            'is_active',
        ]
    
    def get_contributors(self, obj):
        return [user.username for user in obj.Contributor.all()]
