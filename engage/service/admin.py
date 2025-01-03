from django.contrib import admin

from engage.service.models import ServiceType, Service


@admin.register(ServiceType)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'service_type', 'icon', 'link', 'localgovt', 'is_active']
    search_fields = ['title']
    ordering = ['is_active']
    list_filter = ['is_active']
