from django.urls import path

from engage.locations.api.v1.views import ( 
    DivisionListView, 
    DistrictListView, 
    UpazilaListView,
    UnionListView,
)


urlpatterns = [
    path('division-list/', DivisionListView.as_view(), name='division_list'),
    path('district-list/', DistrictListView.as_view(), name='district_list'),
    path('upazila-list/', UpazilaListView.as_view(), name='upazila_list'),
    path('union-list/', UnionListView.as_view(), name='union_list'),
]
