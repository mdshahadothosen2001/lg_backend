from django.contrib import admin

from engage.request.models import Request


@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'requested_citizen', 'localgovt', 'taken_member', 'status', 'possibility_amount', 'possibility_time_required', 'created_at', 'modified_at']
    search_fields = ['title', 'requested_citizen', 'taken_member']
    ordering = ['status']
    list_filter = ['status']
