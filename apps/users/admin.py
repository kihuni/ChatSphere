from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 
                   'is_staff', 'is_online')
    list_filter = ('is_staff', 'is_superuser', 'is_online')
    fieldsets = UserAdmin.fieldsets + (
        ('Profile', {'fields': ('avatar', 'bio', 'status', 'is_online')}),
    )