from django.urls import path, include


urlpatterns = [
    path('v1/', include('engage.notification.api.v1.urls'))
]
