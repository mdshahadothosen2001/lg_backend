from django.contrib import admin

from engage.locations.models import District, Division, Upazila, Union


@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    ordering = ['name']


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ['name', 'division']
    list_filter = ['division']
    search_fields = ['name']
    ordering = ['name']


@admin.register(Upazila)
class UpazilaAdmin(admin.ModelAdmin):
    list_display = ['name', 'district']
    list_filter = ['district__division', 'district']
    search_fields = ['name']
    ordering = ['name']


@admin.register(Union)
class UnionAdmin(admin.ModelAdmin):
    list_display = ['name', 'upazila']
    list_filter = ['upazila__district__division', 'upazila']
    search_fields = ['name']
    ordering = ['name']
