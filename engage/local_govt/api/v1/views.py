import json 

from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from engage.local_govt.api.v1.serializers import MemberSerializer, ContributionSerializer
from engage.local_govt.models import Member, Contribution
from engage.utils.local_govt_utils import find_local_govt


class MemberListAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        union_id = request.query_params.get('union_id')
        member_name = request.query_params.get('member_name')
        members = Member.objects.all()

        if union_id:
            members = members.filter(union_id=union_id)
        if member_name:
            members = members.filter(
                user__name__icontains=member_name
            )

        # If you want to match at least 60% similarity, you can use TrigramSimilarity (requires PostgreSQL)
        # Uncomment the following if using PostgreSQL and django.contrib.postgres
        # from django.contrib.postgres.search import TrigramSimilarity
        # from django.db.models import Q
        # if member_name:
        #     members = members.annotate(
        #         similarity_first=TrigramSimilarity('user__first_name', member_name),
        #         similarity_last=TrigramSimilarity('user__last_name', member_name)
        #     ).filter(
        #         Q(similarity_first__gt=0.6) | Q(similarity_last__gt=0.6)
        #     )

        serializer = MemberSerializer(members, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ContributionListAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        local_govt_id = find_local_govt(request)
        contributions = Contribution.objects.all()
        if local_govt_id:
            contributions = contributions.filter(localgovt__id=local_govt_id)
        serializer = ContributionSerializer(contributions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
