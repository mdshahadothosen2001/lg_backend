from django.urls import path

from engage.request.api.v1.views import RespondAPIView, RespondDetailAPIView


urlpatterns = [
    path('respond/', RespondAPIView.as_view(), name='respond'),
    path('respond/<int:pk>/', RespondDetailAPIView.as_view(), name='respond_detail'),
]
