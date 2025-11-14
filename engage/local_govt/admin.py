from django.contrib import admin
from django.utils.html import format_html

from engage.local_govt.models import Member, Contribution, VoteBooth, Vote



# ----------------------------
#       MEMBERS ADMIN CONFIG
# ----------------------------

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):

    # What to show in the list page
    list_display = (
        'id',
        'position',
        'get_user_name',       # Custom readable user
        'union',
        'areas',
        'start_at',
        'end_at',
        'is_active_badge',     # Custom colored badge
        'is_verified_badge',   # Custom colored badge
    )

    # Filters in sidebar
    list_filter = (
        'is_active',
        'is_verified',
        'union',
        'start_at',
        'end_at',
    )

    # Searchable fields
    search_fields = (
        'position',
        'user__username',
        'user__name',
        'union__name',
        'areas',
    )

    # Ordering
    ordering = ('position',)

    # ---------- Custom display methods ----------

    def get_user_name(self, obj):
        """Display the user's name instead of user object."""
        return obj.user.name if obj.user else "No User"
    get_user_name.short_description = "User"

    def is_active_badge(self, obj):
        """Colored badge for active status."""
        if obj.is_active:
            return format_html(
                '<span style="color: green; font-weight: bold;">✔ Active</span>'
            )
        return format_html(
            '<span style="color: red; font-weight: bold;">✖ Inactive</span>'
        )
    is_active_badge.short_description = "Active Status"
    is_active_badge.admin_order_field = 'is_active'

    def is_verified_badge(self, obj):
        """Colored badge for verified status."""
        if obj.is_verified:
            return format_html(
                '<span style="color: blue; font-weight: bold;">✔ Verified</span>'
            )
        return format_html(
            '<span style="color: gray; font-weight: bold;">✖ Not Verified</span>'
        )
    is_verified_badge.short_description = "Verified"
    is_verified_badge.admin_order_field = 'is_verified'


# ----------------------------
#     CONTRIBUTIONS ADMIN CONFIG
# ----------------------------
@admin.register(Contribution)
class ContributionAdmin(admin.ModelAdmin):

    # Show ALL important fields in list view
    list_display = (
        'project_title',
        'get_contributors',        # M2M display
        'union',
        'areas',
        'start_at',
        'end_at',
        'is_active',
        'member',
    )

    # Filters on sidebar
    list_filter = (
        'is_active',
    )

    # Searchable fields
    search_fields = (
        'project_title',
        'areas',
        'union__name',     # If union has a name field
        'member__name',    # If member has a name field
        'Contributor__username',
    )

    # For easier M2M selection
    filter_horizontal = ('Contributor',)

    # --------- Custom Display Methods ---------

    def get_contributors(self, obj):
        """
        Shows all contributors' names as comma-separated text.
        """
        return ", ".join([user.username for user in obj.Contributor.all()])

    get_contributors.short_description = "Contributors"


# @admin.register(VoteBooth)
# class VoteBoothAdmin(admin.ModelAdmin):
#     list_display = ('vote_title', 'start_at', 'end_at', 'is_active')
#     search_fields = ('vote_title',)
#     list_filter = ('is_active', 'start_at', 'end_at')
#     filter_horizontal = ('candidates', 'voters')


# @admin.register(Vote)
# class VoteAdmin(admin.ModelAdmin):
#     list_display = ('vote_booth', 'voter', 'vote', 'time', 'is_active')
#     search_fields = ('vote_booth__vote_title', 'voter__username')
#     list_filter = ('is_active', 'time')
