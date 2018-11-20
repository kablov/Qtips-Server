from django.db.models import Q
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import *
from qtips.exceptions import *


class PhoneNumberVerificationIfAccountExists(APIView):
    def post(self, request, format = None):
        country_code = request.data['country_code']
        number = request.data['number']
        code = request.data['code']
        phone = Phone.objects.get(Q(country_code = country_code) & Q(number = number))
        code_in_database = str(SmsCode.objects.get(phone = phone).code)
        if code == code_in_database:
            token = Token.objects.get(phone = phone)
            return Response(token.to_dict(), status = status.HTTP_200_OK)
        else:
            raise CodesDoNotMatch("Введенный код не совпадает с отправленным в смс")
