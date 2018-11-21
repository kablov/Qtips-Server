from django.db.models import Q
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import *
from qtips.exceptions import *
from .send_sms import *


class RequestCodeView(APIView):
    def post(self, request, format = None):
        country_code = request.data['country_code']
        number = request.data['number']
        is_sent = False
        if Phone.objects.filter(Q(country_code = country_code) & Q(number = number)).count() == 0:
            phone = Phone()
            phone.country_code = country_code
            phone.number = number
            phone.save()
            sms_code = SmsCode()
            sms_code.phone = phone
            sms_code.save()

            full_phone_number = str(country_code) + str(number)
            text = "Проверочный код: " + sms_code.code
            try:
                send_sms(full_phone_number, text)
            except:
                result = {
                    'is_sent': False
                }
                return Response(result, status = status.HTTP_201_CREATED)

            result = {
                'is_sent': True
            }
            return Response(result, status = status.HTTP_201_CREATED)
        else:
            phone = Phone.objects.get(Q(country_code = country_code) & Q(number = number))
            SmsCode.objects.get(phone = phone).delete()
            sms_code = SmsCode()
            sms_code.phone = phone
            sms_code.save()

            full_phone_number = str(country_code) + str(number)
            text = "Проверочный код: " + sms_code.code
            try:
                send_sms(full_phone_number, text)
            except:
                result = {
                    'is_sent': False
                }
                return Response(result, status = status.HTTP_201_CREATED)

            result = {
                'is_sent': True
            }
            return Response(result, status = status.HTTP_201_CREATED)


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


class PhoneNumberVerificationIfAccountDoesntExist(APIView):
    def post(self, request, format = None):
        country_code = request.data['country_code']
        number = request.data['number']
        code = request.data['code']
        phone = Phone.objects.get(Q(country_code = country_code) & Q(number = number))
        code_in_database = str(SmsCode.objects.get(phone = phone).code)
        if code == code_in_database:
            token = Token()
            token.phone = phone
            token.save()
            return Response(token.to_dict(), status = status.HTTP_201_CREATED)
        else:
            raise CodesDoNotMatch("Введенный код не совпадает с отправленным в смс")
