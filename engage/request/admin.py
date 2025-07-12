from django.contrib import admin

from engage.request.models import Request


@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    def union_display(self, obj):
        if obj.union:
            return f"{obj.union.name} ({obj.union.id})"
        return "No Union"
    union_display.short_description = 'Union'

    list_display = ['id', 'title', 'requested_citizen', 'union_display', 'taken_member', 'status', 'possibility_amount', 'possibility_time_required', 'created_at', 'modified_at']
    list_display_links = ['id', 'title'] 
    search_fields = ['title',] 
    ordering = ['status']
    list_filter = ['status']
