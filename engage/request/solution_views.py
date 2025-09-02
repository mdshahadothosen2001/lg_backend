# views.py
from django.shortcuts import get_object_or_404
from datetime import date, timedelta
from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError, AuthenticationFailed
from engage.utils.jwt_token import decode_jwt
from .models import Solution, SolutionVote, Request
from engage.accounts.models import User
from .serializers import SolutionSerializer, SolutionCreateSerializer, SolutionVoteSerializer


# -------------------------
# Solution List & Create
# -------------------------
class SolutionListCreateView(generics.ListCreateAPIView):
    serializer_class = SolutionSerializer

    def get_queryset(self):
        request_id = self.kwargs.get("request_id")
        return Solution.objects.filter(request=request_id)

    def perform_create(self, serializer):
        request_id = self.kwargs.get("request_id")

        # --- Extract token from header ---
        auth_header = self.request.META.get('HTTP_AUTHORIZATION', '')
        if not auth_header or not auth_header.startswith('Bearer '):
            raise AuthenticationFailed("Authorization token is required.")

        token = auth_header.split(' ', 1)[1].strip()
        try:
            payload = decode_jwt(token)
        except Exception:
            raise AuthenticationFailed("Invalid or expired token.")

        created_by = payload.get("nid")

        req = get_object_or_404(Request, id=request_id)
        user = get_object_or_404(User, id=created_by)

        # Save solution with request + user
        serializer.save(request=req, suggested_by=user)



# -------------------------
# Vote List & Create
# -------------------------
class SolutionVoteListCreateView(generics.ListCreateAPIView):
    """
    - GET: List all votes for a solution
    - POST: User can give a vote (upvote/downvote)
    """
    serializer_class = SolutionVoteSerializer

    def get_queryset(self):
        solution_id = self.kwargs.get("solution_id")
        return SolutionVote.objects.filter(solution_id=solution_id)

    def perform_create(self, serializer):
        solution_id = self.kwargs.get("solution_id")

        auth_header = self.request.META.get('HTTP_AUTHORIZATION', '')
        if auth_header and auth_header.startswith('Bearer '):
            token = auth_header.split(' ', 1)[1].strip()
            try:
                payload = decode_jwt(token)
            except AuthenticationFailed as e:
                # Raised when token is invalid or expired
                raise ValidationError(str(e))
            # payload is available if needed (e.g. payload.get('nid'))
        voted_by = payload.get('nid')
        user = get_object_or_404(User, id=voted_by)

        # Prevent duplicate vote
        if SolutionVote.objects.filter(solution_id=solution_id, voted_by=user).exists():
            raise ValidationError("You have already voted for this solution.")

        serializer.save(solution_id=solution_id, voted_by=user)



# -------------------------
# Problem with Solution for give vote
# 


class SolutionFilterListView(generics.ListAPIView):
    serializer_class = SolutionSerializer

    def get_queryset(self):
        # If Authorization header contains a Bearer token, decode and validate it
        auth_header = self.request.META.get('HTTP_AUTHORIZATION', '')
        if auth_header and auth_header.startswith('Bearer '):
            token = auth_header.split(' ', 1)[1].strip()
            try:
                payload = decode_jwt(token)
            except AuthenticationFailed as e:
                # Raised when token is invalid or expired
                raise ValidationError(str(e))
            # payload is available if needed (e.g. payload.get('nid'))

        queryset = Solution.objects.all().order_by("-created_at")
        filter_type = self.request.query_params.get("filter", None)
        today = date.today()

        if filter_type == "today":
            queryset = queryset.filter(created_at__date=today)

        elif filter_type == "previous_day":
            queryset = queryset.filter(created_at__date=today - timedelta(days=1))

        elif filter_type == "last_week":
            queryset = queryset.filter(created_at__date__gte=today - timedelta(days=7))

        elif filter_type == "last_month":
            queryset = queryset.filter(created_at__date__gte=today - timedelta(days=30))

        elif filter_type == "voted":
            user = self.request.user
            solution_ids = SolutionVote.objects.filter(voted_by=user).values_list("solution_id", flat=True)
            queryset = queryset.filter(id__in=solution_ids)

        return queryset
