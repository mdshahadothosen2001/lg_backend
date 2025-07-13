import json 

from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from engage.local_govt.api.v1.serializers import MemberSerializer, ContributionSerializer
from engage.local_govt.models import Member, Contribution


class MemberListAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        union = request.query_params.get('union')
        member_name = request.query_params.get('name')
        members = Member.objects.all()

        if union:
            members = members.filter(union__id=union)
        elif member_name:
            members = members.filter(
                user__name__icontains=member_name
            )
        else:
            members = members.none()


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
        union = request.query_params.get('union')
        contributions = Contribution.objects.all()
        if union:
            contributions = contributions.filter(union__id=union)
        else:
            contributions = contributions.none()
        serializer = ContributionSerializer(contributions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
