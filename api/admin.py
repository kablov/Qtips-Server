from django.contrib import admin
from api.models import *


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['external_id', 'phone', 'first_name', 'last_name', 'status', 'balance']
    list_per_page = 20
    ordering = ('id',)


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ['country_code', 'number', 'is_verified']
    list_per_page = 20
    ordering = ('id',)


@admin.register(SmsCode)
class SmsCodeAdmin(admin.ModelAdmin):
    list_display = ['phone', 'udid', 'code']
    list_per_page = 20
    ordering = ('id',)


@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    list_display = ['profile', 'token']
    list_per_page = 20
    ordering = ('id',)
