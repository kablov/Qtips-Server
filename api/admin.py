from django.contrib import admin
from api.models import *


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['profile_id', 'phone', 'first_name', 'last_name', 'status']
    list_per_page = 20
    ordering = ('id',)
