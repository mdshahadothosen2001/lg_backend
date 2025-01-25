from django.urls import path, include


urlpatterns = [
    path('v1/', include('engage.request.api.v1.urls'))
]
