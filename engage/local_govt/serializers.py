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
        representation["id"] = instance.user.nid_no if instance.user.nid_no else instance.user.id
        representation['union_name'] = instance.union.name if instance.union else None
        representation['union_id'] = instance.union.id if instance.union else None
        return representation


class ContributionSerializer(serializers.ModelSerializer):
    contributors = serializers.SerializerMethodField()
    union_id = serializers.IntegerField(source='union.id', read_only=True)
    union_name = serializers.CharField(source='union.name', read_only=True)

    class Meta:
        model = Contribution
        fields = [
            'id',
            'project_title',
            'contributors',
            'union_id',
            'union_name',
            'areas',
            'start_at',
            'end_at',
            'is_active',
        ]
    
    def get_contributors(self, obj):
        return [user.name for user in obj.Contributor.all()]
    
    def get_union_id(self, obj):
        return obj.union.id if obj.union else None
    
    def get_union_name(self, obj):
        return obj.union.name if obj.union else None
    