from django.urls import path

from engage.request.views import RespondAPIView, RespondDetailAPIView, RespondImageListView, ActivityListView
from engage.request.solution_views import SolutionListCreateView, SolutionVoteListCreateView, SolutionFilterListView


urlpatterns = [
    path('v1/respond/', RespondAPIView.as_view(), name='respond'),
    path('v1/respond/<int:pk>/', RespondDetailAPIView.as_view(), name='respond_detail'),
    path('respond-images/<int:respond_id>/', RespondImageListView.as_view(), name='respond-images-list'),
    path('activities/<int:respond_id>/', ActivityListView.as_view(), name='activity-list'),
    path('solutions/<int:request_id>/', SolutionListCreateView.as_view(), name='solution-list-create'),
    path('solution/<int:solution_id>/vote/', SolutionVoteListCreateView.as_view(), name='solution-vote-list-create'),
    path("solutions/filter/", SolutionFilterListView.as_view(), name="solution-filter-list"),
]
