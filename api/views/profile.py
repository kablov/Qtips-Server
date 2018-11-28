from django.db.models import Q
from django.shortcuts import render
from django.utils.crypto import get_random_string
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import *
from api.serializers import *
from api.content import *
from qtips.exceptions import *
from qtips.permissions import *
from qtips.decorators import *
import random


class SignUpView(APIView):
    @catch_errors
    def post(self, request, format = None):
        access_key_check(request)
        country_code = request.data['country_code']
        number = request.data['number']
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        photo = request.data['photo']
        udid = request.data['udid']

        if udid == '':
            raise AccessDenied("Нет udid")

        phone = Phone.objects.get(Q(country_code = country_code) & Q(number = number))
        sms_code_udid = SmsCode.objects.get(phone = phone).udid

        if udid != sms_code_udid:
            raise AccessDenied("udids не совпадают")

        if Profile.objects.filter(phone = phone).count() == 0:
            profile = Profile()
            profile.phone = phone
            profile.first_name = first_name
            profile.last_name = last_name
            if photo:
                profile.photo = upload_photo(photo, phone)
            else:
                profile.photo = ''
            profile.save()
            token = Token()
            token.profile = profile
            token.save()
        else:
            raise ProfileEngaged("Аккаунт с указанным номером телефона уже существует")

        token = profile.token.token
        result = {
            'token': token
        }
        return Response(result, status = status.HTTP_201_CREATED)


class ProfilePageView(APIView):
    @catch_errors
    def get(self, request, id, format = None):
        access_key_check(request)
        is_user(request)
        profile = Profile.objects.get(external_id = id)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data, status = status.HTTP_200_OK)

    @catch_errors
    def put(self, request, id, format = None):
        access_key_check(request)
        profile = Profile.objects.get(external_id = id)
        is_owner_or_read_only(request, profile)
        profile = Profile.objects.filter(external_id = id)

        if 'first_name' in request.data:
            new_first_name = request.data['first_name']
            profile.update(first_name = new_first_name)

        if 'last_name' in request.data:
            new_last_name = request.data['last_name']
            profile.update(last_name = new_last_name)

        if 'photo' in request.data:
            new_photo = request.data['photo']
            if new_photo:
                profile.update(photo = upload_photo(new_photo, profile.last().phone))

        serializer = ProfileSerializer(profile, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)


class OwnProfilePageView(APIView):
    @catch_errors
    def get(self, request, format = None):
        access_key_check(request)
        token = Token.objects.get(token = request.META.get('HTTP_AUTHORIZATION'))
        profile = Profile.objects.get(token = token)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data, status = status.HTTP_200_OK)

    @catch_errors
    def put(self, request, format = None):
        access_key_check(request)
        token = Token.objects.get(token = request.META.get('HTTP_AUTHORIZATION'))
        profile = Profile.objects.filter(token = token)

        if 'first_name' in request.data:
            new_first_name = request.data['first_name']
            profile.update(first_name = new_first_name)

        if 'last_name' in request.data:
            new_last_name = request.data['last_name']
            profile.update(last_name = new_last_name)

        if 'photo' in request.data:
            new_photo = request.data['photo']
            if new_photo:
                profile.update(photo = upload_photo(new_photo, profile.last().phone))

        serializer = ProfileSerializer(profile, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
