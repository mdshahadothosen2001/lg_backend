# views.py
from datetime import date, timedelta
from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError
from .models import Solution, SolutionVote
from .serializers import SolutionSerializer, SolutionCreateSerializer, SolutionVoteSerializer


# -------------------------
# Solution List & Create
# -------------------------
class SolutionListCreateView(generics.ListCreateAPIView):
    """
    - GET: List all solutions for a request
    - POST: Create a new solution
    """
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        request_id = self.kwargs.get("request_id")
        return Solution.objects.filter(request_id=request_id).order_by("-created_at")

    def get_serializer_class(self):
        if self.request.method == "POST":
            return SolutionCreateSerializer
        return SolutionSerializer

    def perform_create(self, serializer):
        serializer.save(suggested_by=self.request.user)


# -------------------------
# Vote List & Create
# -------------------------
class SolutionVoteListCreateView(generics.ListCreateAPIView):
    """
    - GET: List all votes for a solution
    - POST: User can give a vote (upvote/downvote)
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SolutionVoteSerializer

    def get_queryset(self):
        solution_id = self.kwargs.get("solution_id")
        return SolutionVote.objects.filter(solution_id=solution_id)

    def perform_create(self, serializer):
        solution_id = self.kwargs.get("solution_id")
        voted_by = self.request.user

        # Prevent duplicate vote
        if SolutionVote.objects.filter(solution_id=solution_id, voted_by=voted_by).exists():
            raise ValidationError("You have already voted for this solution.")

        serializer.save(solution_id=solution_id, voted_by=voted_by)



# -------------------------
# Problem with Solution for give vote
# 


class SolutionFilterListView(generics.ListAPIView):
    serializer_class = SolutionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
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
