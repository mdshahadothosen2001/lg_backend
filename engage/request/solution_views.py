from django.db.models import Q
from django.shortcuts import get_object_or_404
from datetime import date, timedelta
from django.utils import timezone
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

        
        

        # Update voted_users in Solution model to track who voted
        try:
            solution = Solution.objects.get(id=solution_id)
        except Solution.DoesNotExist:
            raise ValidationError("Solution does not exist.")

        user_id = self.request.user.id  # current logged-in user
        solution.voted_users = solution.voted_users or ""

        # Convert comma-separated string -> list of ints
        voted_user_ids = [int(uid) for uid in solution.voted_users.split(",") if uid.strip().isdigit()]

        # Check if user already voted
        if user_id in voted_user_ids:
            raise ValidationError("You have already voted for this solution.")

        # Add the new voter
        voted_user_ids.append(user_id)

        # Convert list back to comma-separated string
        solution.voted_users = ",".join(str(uid) for uid in voted_user_ids)
        solution.save()


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
        auth_header = self.request.META.get('HTTP_AUTHORIZATION', '')
        payload = None
        if auth_header and auth_header.startswith('Bearer '):
            token = auth_header.split(' ', 1)[1].strip()
            try:
                payload = decode_jwt(token)
            except AuthenticationFailed as e:
                raise ValidationError(str(e))

        if not payload:
            return Solution.objects.none()

        user = get_object_or_404(User, id=payload.get('nid'))
        queryset = Solution.objects.filter(is_open_for_vote=True).order_by("-created_at")

        list_type = self.request.query_params.get("list_type")
        now = timezone.now()
        today = now.date()

        # ========== TIME FILTERS ==========
        if list_type == "today":
            start = timezone.datetime.combine(today, timezone.datetime.min.time(), tzinfo=now.tzinfo)
            end = start + timedelta(days=1)
            queryset = queryset.filter(created_at__gte=start, created_at__lt=end)

        elif list_type == "previous_day":
            prev = today - timedelta(days=1)
            start = timezone.datetime.combine(prev, timezone.datetime.min.time(), tzinfo=now.tzinfo)
            end = start + timedelta(days=1)
            queryset = queryset.filter(created_at__gte=start, created_at__lt=end)

        elif list_type == "last_week":
            queryset = queryset.filter(created_at__gte=now - timedelta(days=7))

        elif list_type == "last_month":
            queryset = queryset.filter(created_at__gte=now - timedelta(days=30))

        elif list_type == "voted":
            voted_ids = SolutionVote.objects.filter(voted_by=user).values_list("solution_id", flat=True)
            queryset = queryset.filter(id__in=voted_ids)
            self._list_user_id = user.id
            return queryset

        # ========== EXCLUDE USER-VOTED SOLUTIONS ==========
        voted_ids = SolutionVote.objects.filter(voted_by=user).values_list("solution_id", flat=True)
        queryset = queryset.exclude(id__in=voted_ids)

        self._list_user_id = user.id
        return queryset

    def get_serializer(self, *args, **kwargs):
        # Include user_id in serializer context if set during queryset filtering
        context = self.get_serializer_context()
        if hasattr(self, '_list_user_id'):
            context['user_id'] = self._list_user_id
        kwargs['context'] = context
        return super().get_serializer(*args, **kwargs)

