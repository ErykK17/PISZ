from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    fields = [
        'user',
        'user_type',
        'phone_number',
        'pesel',
        'home_adress',
        'position',
        'department',
        'certificates',
        'family_data',
        'profile_picture',

    ]
