from django.contrib import admin
from .models import Service

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'union', 'is_active')
    list_filter = ('is_active', 'union')
    search_fields = ('title', 'description')
    readonly_fields = ()
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'union', 'link', 'icon', 'is_active')
        }),
    )
