from django.urls import path, include


urlpatterns = [
    path('v1/', include('engage.service.api.v1.urls'))
]
