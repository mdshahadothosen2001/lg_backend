from django.contrib import admin

from engage.service.models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'link', 'localgovt', 'is_active']
    search_fields = ['title']
    ordering = ['is_active']
    list_filter = ['is_active']
