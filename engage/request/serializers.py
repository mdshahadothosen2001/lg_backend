from rest_framework import serializers
from engage.request.models import Request

from engage.request.models import RespondImage


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



class RespondImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RespondImage
        fields = ['id', 'respond', 'image']




# Solution and Vote Serializers

from .models import Solution, SolutionVote


class SolutionSerializer(serializers.ModelSerializer):
    votes_count = serializers.SerializerMethodField()
    request_title = serializers.SerializerMethodField()

    class Meta:
        model = Solution
        fields = ['id', 'request', 'request_title', 'suggested_by', 'description', 'file',
                  'is_best', 'is_open_for_vote', 'created_at', 'votes_count']

    def get_votes_count(self, obj):
        upvotes = obj.votes.filter(value=True).count()
        downvotes = obj.votes.filter(value=False).count()
        return {"upvotes": upvotes, "downvotes": downvotes}

    def get_request_title(self, obj):
        return obj.request.title if getattr(obj, 'request', None) else None


class SolutionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solution
        fields = ['request', 'description', 'file']


class SolutionVoteSerializer(serializers.ModelSerializer):
    solution_id = serializers.SerializerMethodField()
    solution_description = serializers.SerializerMethodField()
    solution_request_title = serializers.SerializerMethodField()

    class Meta:
        model = SolutionVote
        fields = ['id', 'solution', 'solution_id', 'solution_description', 'solution_request_title', 'voted_by', 'value', 'created_at']
        read_only_fields = ['voted_by', 'solution']

    def get_solution_id(self, obj):
        return obj.solution.id if getattr(obj, 'solution', None) else None

    def get_solution_description(self, obj):
        return obj.solution.description if getattr(obj, 'solution', None) else None

    def get_solution_request_title(self, obj):
        if not getattr(obj, 'solution', None):
            return None
        req = getattr(obj.solution, 'request', None)
        return req.title if req else None

