"""Configuration of the admin interface for clubs."""
from django.contrib import admin
from .models import Member

# Register your models here.
@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = [
        'first_name', 'last_name', 'email', 'bio', 'experience_level', 'personal_statement',
    ]