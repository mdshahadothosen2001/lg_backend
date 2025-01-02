from django.contrib import admin

from engage.local_govt.models import Localgovt, Member


@admin.register(Localgovt)
class LocalgovtAdmin(admin.ModelAdmin):
    list_display = ['id', 'type', 'division', 'district', 'upazila', 'union', 'location', 'description']
    search_fields = ['type']
    ordering = ['type']


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['id', 'position', 'user', 'localgovt', 'areas', 'start_at', 'end_at', 'is_active']
    search_fields = ['position']
    ordering = ['position']
