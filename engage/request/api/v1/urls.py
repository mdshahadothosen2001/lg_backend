from django.urls import path

from engage.request.api.v1.views import RespondAPIView


urlpatterns = [
    path('respond/', RespondAPIView.as_view(), name='respond'),
]
