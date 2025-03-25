from django.contrib import admin
from .models import Notice, Event

@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'localgovt', 'is_active')
    search_fields = ('title',)
    list_filter = ('is_active', 'localgovt')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'start', 'duration', 'localgovt', 'is_active')
    search_fields = ('title',)
    list_filter = ('is_active', 'localgovt')