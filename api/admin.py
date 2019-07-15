from django.contrib import admin
from api.models import Profile, Phone, SmsCode, Token, Transaction, WithdrawRequest


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'external_id', 'phone', 'first_name', 'last_name',
                    'email', 'status', 'balance', 'are_notifications_enabled']
    list_per_page = 20
    ordering = ('-id',)


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ['country_code', 'number', 'is_verified']
    list_per_page = 20
    ordering = ('-id',)


@admin.register(SmsCode)
class SmsCodeAdmin(admin.ModelAdmin):
    list_display = ['phone', 'udid', 'code']
    list_per_page = 20
    ordering = ('-id',)


@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    list_display = ['profile', 'token']
    list_per_page = 20
    ordering = ('-id',)


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['recipient', 'type', 'amount', 'time']
    list_per_page = 20
    ordering = ('-id',)


@admin.register(WithdrawRequest)
class WithdrawRequestAdmin(admin.ModelAdmin):
    list_display = ['profile', 'amount', 'request_date', 'status', 'reviewed_time']
    list_per_page = 20
    ordering = ('-id',)
