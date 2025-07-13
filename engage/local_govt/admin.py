from django.contrib import admin

from engage.local_govt.models import Member, Contribution, VoteBooth, Vote



@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['id', 'position', 'user', 'union', 'is_verified', 'areas', 'start_at', 'end_at', 'is_active']
    search_fields = ['position']
    ordering = ['position']


@admin.register(Contribution)
class ContributionAdmin(admin.ModelAdmin):
    list_display = ('project_title', 'start_at', 'end_at', 'is_active')
    list_filter = ('is_active', 'start_at', 'end_at')
    search_fields = ('project_title', 'areas')
    filter_horizontal = ('Contributor',)


@admin.register(VoteBooth)
class VoteBoothAdmin(admin.ModelAdmin):
    list_display = ('vote_title', 'start_at', 'end_at', 'is_active')
    search_fields = ('vote_title',)
    list_filter = ('is_active', 'start_at', 'end_at')
    filter_horizontal = ('candidates', 'voters')


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ('vote_booth', 'voter', 'vote', 'time', 'is_active')
    search_fields = ('vote_booth__vote_title', 'voter__username')
    list_filter = ('is_active', 'time')
