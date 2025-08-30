# admin.py
from django.contrib import admin
from django.utils.html import format_html
from engage.request.models import Request, RespondImage, Solution, SolutionVote


# -------------------------
# Inline for RespondImage
# -------------------------
class RespondImageInline(admin.TabularInline):
    model = RespondImage
    extra = 1
    fields = ['image', 'image_preview']
    readonly_fields = ['image_preview']

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height: 80px;"/>', obj.image.url)
        return "No Image"
    image_preview.short_description = 'Preview'


# -------------------------
# Solution Inline (inside Request)
# -------------------------
class SolutionInline(admin.TabularInline):
    model = Solution
    extra = 1
    fields = ['suggested_by', 'description', 'file', 'is_open_for_vote', 'is_best']
    readonly_fields = []
    show_change_link = True  # solution এ link দিবে যাতে edit page এ যাওয়া যায়


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

    inlines = [RespondImageInline, SolutionInline]


# -------------------------
# Solution Admin
# -------------------------
@admin.register(Solution)
class SolutionAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'request', 'suggested_by', 'short_description',
        'is_open_for_vote', 'is_best', 'created_at'
    ]
    list_filter = ['is_open_for_vote', 'is_best']
    search_fields = ['description', 'suggested_by__username']

    def short_description(self, obj):
        return (obj.description[:50] + "...") if len(obj.description) > 50 else obj.description
    short_description.short_description = "Description"


# -------------------------
# SolutionVote Admin
# -------------------------
@admin.register(SolutionVote)
class SolutionVoteAdmin(admin.ModelAdmin):
    list_display = ['id', 'solution', 'voted_by', 'value', 'created_at']
    list_filter = ['value']
    search_fields = ['solution__description', 'voted_by__username']
