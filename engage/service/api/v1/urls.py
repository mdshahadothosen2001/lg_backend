from django.urls import path

from engage.service.api.v1.views import ServiceTypeListView, ServiceListView


urlpatterns = [
    path('localgovt-service-type-list/', ServiceTypeListView.as_view(), name='localgovt_service_type_list'),
    path('localgovt-service-list/', ServiceListView.as_view(), name='localgovt_service_list'),
]
