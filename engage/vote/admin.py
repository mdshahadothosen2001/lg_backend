from django.contrib import admin

from engage.vote.models import VotingPoll, Voting


@admin.register(VotingPoll)
class VotingPollAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_by', 'description', 'total_voter', 'start_date', 'end_date', 'is_public', 'is_voting', 'is_result_published', 'is_active', 'created_at', 'modified_at']
    search_fields = ['title', ]
    ordering = ['is_active']
    list_filter = ['is_active']


@admin.register(Voting)
class VotingAdmin(admin.ModelAdmin):
    list_display = ['id', 'voter', 'votingpoll', 'opinion', 'created_at', 'modified_at']
    search_fields = ['votingpoll']
    ordering = ['opinion']
    list_filter = ['opinion']
