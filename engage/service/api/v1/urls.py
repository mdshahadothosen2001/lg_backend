from django.urls import path

from engage.service.api.v1.views import ServiceListView


urlpatterns = [
    path('localgovt-service-list/', ServiceListView.as_view(), name='localgovt_service_list'),
]
