from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.forms import CustomUserCreationForm, CustomUserChangeForm
from users.models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ('email', 'is_staff', 'is_active', 'last_name')
    list_filter = ('email', 'is_staff', 'is_active', 'last_name')
    fieldsets = (
    (
        None,
        {
            'fields': (
                'email',
                'password',
                'first_name',
                'last_name',
                'gender',
                'birth_date'
            )
        }
    ),
        (
            'Permissions',
            {
                'fields': (
                    'is_staff',
                    'is_active'
                )
            }
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    'email',
                    'first_name',
                    'last_name',
                    'gender',
                    'birth_date',
                    'password1',
                    'password2',
                    'is_staff',
                    'is_active'
                )
            }
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)

# Register your models here.
