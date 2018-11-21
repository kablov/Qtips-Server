from django.db.models import Q
from django.shortcuts import render
from django.utils.crypto import get_random_string
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import *
from api.serializers import *
from qtips.exceptions import *
from qtips.permissions import *
import random


class SignUpView(APIView):
    def post(self, request, format = None):
        country_code = request.data['country_code']
        number = request.data['number']
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        photo = request.data['photo']

        if country_code == '':
            raise CountryCodeNotEntered("Не введен код страны")
        if number == '':
            raise NumberNotEntered("Не введен номер")
        if first_name == '':
            raise FirstNameNotEntered("Не введено имя")
        if last_name == '':
            raise LastNameNotEntered("Не введена фамилия")

        if Phone.objects.filter(Q(country_code = country_code) & Q(number = number)).count() == 0:
            phone = Phone()
            phone.country_code = country_code
            phone.number = number
            phone.save()

            profile = Profile()
            profile.phone = phone
            profile.first_name = first_name
            profile.last_name = last_name
            profile.photo = photo
            profile.save()

        elif Phone.objects.filter(Q(country_code = country_code) & Q(number = number)).count() > 0 and Profile.objects.filter(phone = Phone.objects.get(Q(country_code = country_code) & Q(number = number))).count() == 0:
            phone = Phone.objects.get(Q(country_code = country_code) & Q(number = number))
            profile = Profile()
            profile.phone = phone
            profile.first_name = first_name
            profile.last_name = last_name
            profile.photo = photo
            profile.save()

        else:
            raise PhoneEngaged("Аккаунт с таким номером телефона уже существует")

        serializer = ProfileSerializer(profile)
        return Response(serializer.data, status = status.HTTP_201_CREATED)


class ProfilePageView(APIView):

    def get(self, request, id, format = None):
        is_user(request)
        profile = Profile.objects.get(external_id = id)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def put(self, request, id, format = None):
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
            profile.update(photo = new_photo)

        serializer = ProfileSerializer(profile, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
