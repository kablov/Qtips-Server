from django.contrib import admin
from api.models import Profile, Phone, SmsCode, Token, Transaction, \
    WithdrawRequest


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'external_id', 'phone', 'first_name', 'last_name',
                    'email', 'status', 'balance', 'are_notifications_enabled']
    search_fields = ['external_id', 'first_name', 'last_name', 'email',
                     'phone__number']
    list_filter = ['status', 'balance']
    list_per_page = 20
    ordering = ('-id',)


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ['country_code', 'number', 'is_verified']
    search_fields = ['country_code', 'number']
    list_filter = ['is_verified']
    list_per_page = 20
    ordering = ('-id',)


@admin.register(SmsCode)
class SmsCodeAdmin(admin.ModelAdmin):
    list_display = ['phone', 'udid', 'code']
    search_fields = ['udid', 'phone__number']
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
    search_fields = ['recipient__first_name', 'recipient__last_name',
                     'recipient__phone__number']
    list_filter = ['type', 'time']
    list_per_page = 20
    ordering = ('-id',)


@admin.register(WithdrawRequest)
class WithdrawRequestAdmin(admin.ModelAdmin):
    list_display = [
        'profile', 'amount', 'request_date', 'status', 'reviewed_time'
    ]
    search_fields = ['profile__first_name', 'profile__last_name',
                     'profile__phone__number']
    list_filter = ['request_date', 'reviewed_time', 'status']
    list_per_page = 20
    ordering = ('-id',)
