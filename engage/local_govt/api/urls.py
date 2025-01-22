from django.urls import path, include


urlpatterns = [
    path('v1/', include('engage.local_govt.api.v1.urls'))
]
