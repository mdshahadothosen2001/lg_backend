from django.contrib import admin
from .models import Notice, Even

@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'localgovt', 'is_active')
    list_filter = ('is_active', 'localgovt')
    search_fields = ('title',),

@admin.register(Even)
class EvenAdmin(admin.ModelAdmin):
    list_display = ('title', 'start', 'link', 'localgovt', 'is_active')
    list_filter = ('is_active', 'localgovt')
    search_fields = ('title',),