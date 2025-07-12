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
        return obj.user.name if obj.user else None
    
    def get_picture(self, obj):
        return f"{obj.user.picture} {obj.user.picture}"
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['union_name'] = instance.localgovt.union.name if instance.localgovt.union else None
        representation['union_id'] = instance.localgovt.union.id if instance.localgovt.union else None
        return representation


class ContributionSerializer(serializers.ModelSerializer):
    contributors = serializers.SerializerMethodField()
    local_govt = serializers.SerializerMethodField()

    class Meta:
        model = Contribution
        fields = [
            'id',
            'project_title',
            'contributors',
            'local_govt',
            'areas',
            'start_at',
            'end_at',
            'is_active',
        ]
    
    def get_contributors(self, obj):
        return [user.username for user in obj.Contributor.all()]
    
    def get_local_govt(self, obj):
        localgovt = obj.localgovt.division.name
        if obj.localgovt.district:
            localgovt += '-'+ obj.localgovt.district.name
        if obj.localgovt.upazila:
            localgovt += '-'+ obj.localgovt.upazila.name
        if obj.localgovt.union:
            localgovt += '-'+ obj.localgovt.union.name

        return localgovt