from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("ces/", admin.site.urls),
    path('locations/api/', include('engage.locations.api.urls')),
    path('local-govt/api/', include('engage.local_govt.urls')),
    path('respond/api/', include('engage.request.urls')),
    path('notice/api/', include('engage.notification.api.urls')),
    path('api/user/', include('engage.accounts.urls')),
    path('api/service/', include('engage.service.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]