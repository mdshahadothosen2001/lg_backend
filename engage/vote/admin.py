from django.contrib import admin

from engage.vote.models import VotingPoll, Voting


@admin.register(VotingPoll)
class VotingPollAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_by', 'localgovt', 'description', 'total_voter', 'is_active', 'created_at', 'modified_at']
    search_fields = ['title', 'localgovt']
    ordering = ['is_active']
    list_filter = ['is_active']


@admin.register(Voting)
class VotingAdmin(admin.ModelAdmin):
    list_display = ['id', 'voter', 'votingpoll', 'opinion', 'created_at', 'modified_at']
    search_fields = ['votingpoll']
    ordering = ['opinion']
    list_filter = ['opinion']
