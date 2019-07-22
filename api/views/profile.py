import requests
from django.db.models import Q
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Profile, Token, Phone, SmsCode
from api.serializers import ProfileSerializer
from api.content import upload_photo, upload_qr
from qtips import settings
from qtips.decorators import catch_errors
from qtips.permissions import access_key_check
from qtips.exceptions import AccessDenied, ProfileEngaged


class SignUpView(APIView):
    @catch_errors
    def post(self, request, format=None):
        access_key_check(request)
        country_code = request.data['country_code']
        number = request.data['number']
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        email = request.data['email']
        if 'photo' in request.FILES:
            photo = request.data['photo']
        else:
            photo = ''
        udid = request.data['udid']

        if udid == '':
            raise AccessDenied("Нет udid")

        phone = Phone.objects.get(
            Q(country_code=country_code) & Q(number=number)
        )
        sms_code_udid = SmsCode.objects.get(phone=phone).udid

        if udid != sms_code_udid:
            raise AccessDenied("udids не совпадают")

        if Profile.objects.filter(phone=phone).count() == 0:
            profile = Profile()
            profile.phone = phone
            profile.first_name = first_name
            profile.last_name = last_name
            profile.email = email
            if photo:
                profile.photo = upload_photo(photo, phone)
            else:
                profile.photo = ''
            host = request.META['HTTP_HOST']
            if host.startswith('www.'):
                host = host[4:]
            profile.payment_url = host + "/" + str(profile.external_id)
            qr = requests.get('https://api.scanova.io/v2/qrcode/url' + '?url='
                              + profile.payment_url + '&apikey='
                              + settings.SCANOVA_API_KEY)
            profile.qr = upload_qr(qr.content, phone)
            profile.save()

            token = Token()
            token.profile = profile
            token.save()

        else:
            raise ProfileEngaged(
                "Аккаунт с указанным номером телефона уже существует")

        token = profile.token.token
        result = {
            'token': token
        }
        return Response(result, status=status.HTTP_201_CREATED)


class ProfilePageView(APIView):
    @catch_errors
    def get(self, request, format=None):
        access_key_check(request)
        token = Token.objects.get(
            token=request.META.get('HTTP_AUTHORIZATION')[6:]
        )
        profile = Profile.objects.get(token=token)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @catch_errors
    def put(self, request, format=None):
        access_key_check(request)
        token = Token.objects.get(
                token=request.META.get('HTTP_AUTHORIZATION')[6:]
        )
        profile = Profile.objects.filter(token=token)

        if 'first_name' in request.data:
            new_first_name = request.data['first_name']
            profile.update(first_name=new_first_name)

        if 'last_name' in request.data:
            new_last_name = request.data['last_name']
            profile.update(last_name=new_last_name)

        if 'email' in request.data:
            new_email = request.data['email']
            profile.update(email=new_email)

        if 'photo' in request.data:
            new_photo = request.data['photo']
            if new_photo:
                profile.update(
                    photo=upload_photo(new_photo, profile.last().phone)
                )

        profile = Profile.objects.get(token=token)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SwitchNotificationsView(APIView):
    @catch_errors
    def post(self, request, format=None):
        access_key_check(request)
        token = Token.objects.get(
            token=request.META.get('HTTP_AUTHORIZATION')[6:]
        )
        profile = Profile.objects.get(token=token)
        are_notifications_enabled = request.data['is_on']

        profile.are_notifications_enabled = are_notifications_enabled
        profile.save(update_fields=['are_notifications_enabled'])

        return Response("Настройки уведомлений сохранены",
                        status=status.HTTP_201_CREATED)
