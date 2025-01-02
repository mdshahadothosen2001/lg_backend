from django.urls import path, include


urlpatterns = [
    path('v1/', include('engage.locations.api.v1.urls'))
]
