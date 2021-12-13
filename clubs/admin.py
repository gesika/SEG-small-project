from django.contrib import admin
from .models import User, UserProfile

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
     list_display = [
        'email', 'first_name', 'last_name', 'bio', 'is_active',
    ]
     list_display_links = ('email',)

admin.site.register(UserProfile)