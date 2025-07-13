from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path('locations/api/', include('engage.locations.api.urls')),
    path('local-govt/api/', include('engage.local_govt.api.urls')),
    path('respond/api/', include('engage.request.api.urls')),
    path('notice/api/', include('engage.notification.api.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]