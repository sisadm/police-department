from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['id', 'username', 'email', 'role']
    search_fields = ['id', 'username', 'email', 'role']
    list_filter = ['role', 'is_staff', 'is_active', 'date_joined']
    readonly_fields = ['last_login', 'date_joined']
    ordering = ['id']


    fieldsets = (
        (None, {'fields': ('email', 'username', 'password', 'role')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'role'),
        }),
    )



    