from django.contrib import admin

from engage.local_govt.models import Localgovt, Member, Contribution, VoteBooth, Vote


@admin.register(Localgovt)
class LocalgovtAdmin(admin.ModelAdmin):
    list_display = ['id', 'type', 'division', 'district', 'upazila', 'union', 'location', 'description']
    search_fields = ['type']
    ordering = ['type']


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['id', 'position', 'user', 'union_id', 'union_name', 'is_verified', 'localgovt', 'areas', 'start_at', 'end_at', 'is_active']
    search_fields = ['position']
    ordering = ['position']


@admin.register(Contribution)
class ContributionAdmin(admin.ModelAdmin):
    list_display = ('project_title', 'localgovt', 'start_at', 'end_at', 'is_active')
    list_filter = ('is_active', 'start_at', 'end_at', 'localgovt')
    search_fields = ('project_title', 'localgovt__type', 'areas')
    filter_horizontal = ('Contributor',)


@admin.register(VoteBooth)
class VoteBoothAdmin(admin.ModelAdmin):
    list_display = ('vote_title', 'localgovt', 'start_at', 'end_at', 'is_active')
    search_fields = ('vote_title', 'localgovt__type', 'localgovt__division__name')
    list_filter = ('is_active', 'start_at', 'end_at')
    filter_horizontal = ('candidates', 'voters')


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ('vote_booth', 'voter', 'vote', 'time', 'is_active')
    search_fields = ('vote_booth__vote_title', 'voter__username')
    list_filter = ('is_active', 'time')
