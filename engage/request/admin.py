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
            return format_html('<img src="{}" style="height:80px; border-radius:5px;" />', obj.image.url)
        return "No Image"
    image_preview.short_description = 'Preview'


# -------------------------
# Solution Inline (inside Request)
# -------------------------
class SolutionInline(admin.TabularInline):
    model = Solution
    extra = 1
    fields = ['suggested_by', 'short_description', 'file_link', 'is_open_for_vote', 'is_best']
    readonly_fields = ['short_description', 'file_link']
    show_change_link = True  # Makes each solution clickable to edit page

    def short_description(self, obj):
        return (obj.description[:50] + '...') if len(obj.description) > 50 else obj.description
    short_description.short_description = "Description"

    def file_link(self, obj):
        if obj.file:
            return format_html('<a href="{}" target="_blank">Open File</a>', obj.file)
        return "-"
    file_link.short_description = "File"


# -------------------------
# Request Admin
# -------------------------
@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):

    list_display = [
        'id', 'title', 'requested_citizen', 'union_display', 'taken_member',
        'status_badge', 'possibility_amount', 'possibility_time_required',
        'created_at', 'modified_at'
    ]
    list_display_links = ['id', 'title']
    search_fields = ['title', 'description', 'requested_citizen__username', 'taken_member__user__username']
    ordering = ['-created_at']
    list_filter = ['status', 'union', 'taken_member']

    inlines = [RespondImageInline, SolutionInline]

    def union_display(self, obj):
        if obj.union:
            return f"{obj.union.name} ({obj.union.id})"
        return "No Union"
    union_display.short_description = 'Union'

    def status_badge(self, obj):
        color = {
            'pending': 'gray',
            'acepted': 'blue',
            'canceled': 'red',
            'on_progress': 'orange',
            'done': 'green'
        }.get(obj.status, 'black')
        return format_html('<span style="color:{}; font-weight:bold;">{}</span>', color, obj.status.capitalize())
    status_badge.short_description = "Status"


# -------------------------
# Solution Admin
# -------------------------
@admin.register(Solution)
class SolutionAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'request_link', 'suggested_by', 'short_description',
        'file_link', 'is_open_for_vote_badge', 'is_best_badge', 'created_at'
    ]
    list_filter = ['is_open_for_vote', 'is_best']
    search_fields = ['description', 'suggested_by__username', 'request__title']

    def short_description(self, obj):
        return (obj.description[:50] + "...") if len(obj.description) > 50 else obj.description
    short_description.short_description = "Description"

    def request_link(self, obj):
        return format_html('<a href="/ces/request/request/{}/change/">{}</a>', obj.request.id, obj.request.title)
    request_link.short_description = "Request"

    def file_link(self, obj):
        if obj.file:
            return format_html('<a href="{}" target="_blank">Open File</a>', obj.file)
        return "-"
    file_link.short_description = "File"

    def is_open_for_vote_badge(self, obj):
        color = 'green' if obj.is_open_for_vote else 'gray'
        return format_html('<span style="color:{};">{}</span>', color, obj.is_open_for_vote)
    is_open_for_vote_badge.short_description = "Voting Open"

    def is_best_badge(self, obj):
        color = 'blue' if obj.is_best else 'gray'
        return format_html('<span style="color:{};">{}</span>', color, obj.is_best)
    is_best_badge.short_description = "Best Solution"


# -------------------------
# SolutionVote Admin
# -------------------------
@admin.register(SolutionVote)
class SolutionVoteAdmin(admin.ModelAdmin):
    list_display = ['id', 'solution_link', 'voted_by', 'value_badge', 'created_at']
    list_display_links = ['id', 'solution_link']
    list_filter = ['value']
    search_fields = ['solution__description', 'voted_by__username']

    def solution_link(self, obj):
        return format_html('<a href="/ces/request/solution/{}/change/">{}</a>', obj.solution.id, obj.solution)
    solution_link.short_description = "Solution"

    def value_badge(self, obj):
        color = 'green' if obj.value else 'red'
        return format_html('<span style="color:{}; font-weight:bold;">{}</span>', color, 'Upvote' if obj.value else 'Downvote')
    value_badge.short_description = "Vote"
