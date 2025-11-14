from django.contrib import admin
from django.utils.html import format_html

from .models import Service


# -----------------------------
# Service Admin
# -----------------------------
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'title',
        'union',
        'short_description',
        'link_clickable',
        'icon_preview',
        'is_active_badge',
    )

    list_display_links = ('id', 'title')

    list_filter = ('is_active', 'union')
    search_fields = ('title', 'description', 'union__name')

    readonly_fields = ('icon_preview_large', 'link_clickable_field')

    fieldsets = (
        (None, {
            'fields': (
                'title',
                'description',
                'union',
                'link',
                'link_clickable_field',   # show clickable link in form
                'icon',
                'icon_preview_large',
                'is_active',
            )
        }),
    )

    # -----------------------------
    # Custom Display Methods
    # -----------------------------

    def link_clickable(self, obj):
        """Clickable link in list view."""
        if obj.link:
            return format_html('<a href="{}" target="_blank">Open Link</a>', obj.link)
        return "-"
    link_clickable.short_description = "Link"

    def link_clickable_field(self, obj):
        """Clickable link inside form."""
        if obj.link:
            return format_html('<a href="{}" target="_blank">Click to open link</a>', obj.link)
        return "No link added."
    link_clickable_field.short_description = "Preview Link"

    def short_description(self, obj):
        if not obj.description:
            return "-"
        return (obj.description[:40] + " ...") if len(obj.description) > 40 else obj.description
    short_description.short_description = "Description"

    def icon_preview(self, obj):
        if obj.icon:
            return format_html('<img src="{}" width="40" height="40" style="border-radius:5px;" />', obj.icon.url)
        return "-"
    icon_preview.short_description = "Icon"

    def icon_preview_large(self, obj):
        if obj.icon:
            return format_html('<img src="{}" width="120" style="border-radius:8px; margin-top:5px;" />', obj.icon.url)
        return "No icon uploaded."
    icon_preview_large.short_description = "Icon Preview"

    def is_active_badge(self, obj):
        if obj.is_active:
            return format_html('<span style="color: green; font-weight: bold;">✔ Active</span>')
        return format_html('<span style="color: red; font-weight: bold;">✖ Inactive</span>')
    is_active_badge.short_description = "Status"