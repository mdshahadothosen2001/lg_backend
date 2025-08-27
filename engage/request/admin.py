# admin.py
from django.contrib import admin
from django.utils.html import format_html
from engage.request.models import Request, RespondImage


# -------------------------
# Inline for RespondImage
# -------------------------
class RespondImageInline(admin.TabularInline):
    model = RespondImage
    extra = 1  # kotota extra blank form show korbe
    fields = ['image', 'image_preview']  # show image & preview
    readonly_fields = ['image_preview']  # preview read-only

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height: 80px;"/>', obj.image.url)
        return "No Image"
    image_preview.short_description = 'Preview'


# -------------------------
# Request Admin
# -------------------------
@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    def union_display(self, obj):
        if obj.union:
            return f"{obj.union.name} ({obj.union.id})"
        return "No Union"
    union_display.short_description = 'Union'

    list_display = [
        'id', 'title', 'requested_citizen', 'union_display', 'taken_member', 
        'status', 'possibility_amount', 'possibility_time_required', 
        'created_at', 'modified_at'
    ]
    list_display_links = ['id', 'title'] 
    search_fields = ['title'] 
    ordering = ['status']
    list_filter = ['status']

    inlines = [RespondImageInline]  # Inline add
