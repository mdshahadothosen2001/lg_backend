from django.urls import path

from engage.local_govt.views import MemberListAPIView, ContributionListAPIView


urlpatterns = [
    path('v1/member-list/', MemberListAPIView.as_view(), name='member_list_or_create'),
    path('v1/contribution/', ContributionListAPIView.as_view(), name='contribution'),
]
