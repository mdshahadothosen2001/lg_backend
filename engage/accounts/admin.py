from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Permission
from django.utils.translation import gettext_lazy as _

from engage.accounts.models import User, UserPermanentAddress

admin.site.register(Permission)


class UserPermanentAddressInline(admin.StackedInline):
    model = UserPermanentAddress
    extra = 0


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = [
        (None, {'fields': ['username', 'password']}),
        (_('Personal info'), {
            'fields': [
                'first_name',
                'last_name',
                'date_of_birth',
                'birth_no',
                'nid_no',
                'gender',
                'religion',
                ('email', 'email_verified'),
                ('mobile_number', 'mobile_verified'),
            ]
        }),
        (_('Family info'), {
            'fields': [
                'father_name',
                'father_nid_no',
                'mother_name',
                'mother_nid_no',
            ]
        }),
        (_('Permissions'), {
            'fields': ['is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions']
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    ]
    add_fieldsets = [
        (None, {
            'classes': ['wide'],
            'fields': ['username', 'password1', 'password2'],
        })
    ]
    list_display = ['username', 'mobile_number', 'email', 'first_name', 'last_name', 'is_staff']
    list_filter = [
        'is_active',
        'email_verified',
        'mobile_verified',
        'is_staff',
        'is_superuser',
    ]
    search_fields = ['email', 'mobile_number', 'first_name', 'last_name']
    filter_horizontal = ['groups', 'user_permissions']
    ordering = ['-id']
    inlines = [UserPermanentAddressInline]
