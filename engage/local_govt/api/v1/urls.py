from django.urls import path

from engage.local_govt.api.v1.views import MemberListAPIView, ContributionListAPIView


urlpatterns = [
    path('member-list/', MemberListAPIView.as_view(), name='member_list_or_create'),
    path('contribution/', ContributionListAPIView.as_view(), name='contribution'),
]
