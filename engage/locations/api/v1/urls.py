from django.urls import path

from engage.locations.api.v1.views import ( 
    DivisionCreateView, 
    DistrictCreateView, 
    UpazilaCreateView, 
    UnionCreateView, 
    DivisionListView, 
    DistrictListView, 
    UpazilaListView,
    UnionListView,
)


urlpatterns = [
    path('division-create/', DivisionCreateView.as_view(), name='division_create'),
    path('district-create/', DistrictCreateView.as_view(), name='district_create'),
    path('upazila-create/', UpazilaCreateView.as_view(), name='upazila_create'),
    path('union-create/', UnionCreateView.as_view(), name='union_create'),
    path('division-list/', DivisionListView.as_view(), name='division_list'),
    path('district-list/', DistrictListView.as_view(), name='district_list'),
    path('upazila-list/', UpazilaListView.as_view(), name='upazila_list'),
    path('union-list/', UnionListView.as_view(), name='union_list'),
]
