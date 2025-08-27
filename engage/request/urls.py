from django.urls import path

from engage.request.views import RespondAPIView, RespondDetailAPIView, RespondImageListView


urlpatterns = [
    path('v1/respond/', RespondAPIView.as_view(), name='respond'),
    path('v1/respond/<int:pk>/', RespondDetailAPIView.as_view(), name='respond_detail'),
    path('respond-images/<int:respond_id>/', RespondImageListView.as_view(), name='respond-images-list'),
]
