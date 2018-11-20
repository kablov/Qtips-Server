from django.contrib import admin
from django.urls import path
from api.views import *


urlpatterns = [
    path('auth/', profile.AuthView.as_view()),
    path('signup/', profile.SignUpView.as_view()),
    path('profile/<int:id>/', profile.ProfilePageView.as_view()),
    path('code/', sms_code.PhoneNumberVerificationIfAccountExists.as_view()),
    path('auth/code/', sms_code.PhoneNumberVerificationIfAccountDoesntExist.as_view()),
]
