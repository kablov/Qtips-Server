from django.db.models import Q
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Profile, Token, Phone, SmsCode
from qtips.decorators import catch_errors
from qtips.permissions import access_key_check
from qtips.exceptions import AccessDenied, ProfileEngaged
from api.content import send_sms


class RequestCodeView(APIView):
    @catch_errors
    def post(self, request, format = None):
        access_key_check(request)
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
            text = "Проверочный код для Qtips: " + sms_code.code
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


class PhoneNumberVerificationView(APIView):
    @catch_errors
    def post(self, request, format = None):
        access_key_check(request)
        country_code = request.data['country_code']
        number = request.data['number']
        code = request.data['code']
        udid = request.data['udid']
        phone = Phone.objects.get(Q(country_code = country_code) & Q(number = number))
        code_in_database = str(SmsCode.objects.get(phone = phone).code)
        if code == code_in_database:
            phone.is_verified = True
            phone.save(update_fields=['is_verified'])
            sms_code = SmsCode.objects.get(code = code)
            sms_code.udid = udid
            sms_code.save(update_fields = ['udid'])
            if Profile.objects.filter(phone = phone).count() > 0:
                profile = Profile.objects.get(phone = phone)
                token = Token.objects.get(profile = profile).token
                result = {
                    'is_verified': True,
                    'token': token
                }
            else:
                result = {
                    'is_verified': True
                }
            return Response(result, status = status.HTTP_200_OK)
        else:
            result = {
                'is_verified': False
            }
            return Response(result, status = status.HTTP_200_OK)
