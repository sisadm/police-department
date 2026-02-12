from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['id', 'username', 'email', 'role']
    search_fields = ['id', 'username', 'email']

admin.site.register(User, CustomUserAdmin)