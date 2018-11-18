from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import *
from api.serializers import *
from qtips.exceptions import *
import random


class AuthView(APIView):
    def post(self, request, format = None):
        country_code = request.data['country_code']
        number = request.data['number']
        phones = Phone.objects.all()
        is_registered = False
        for phone in phones:
            if country_code == phone.country_code and number == phone.number:
                is_registered = True
                break
        return Response(is_registered, status = status.HTTP_200_OK)


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

        phones = Phone.objects.all()
        is_registered = False
        for phone in phones:
            if country_code == phone.country_code and number == phone.number:
                is_registered = True
                break

        if is_registered == False:
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
        else:
            raise PhoneEngaged("Аккаунт с таким номером телефона уже существует")

        serializer = ProfileSerializer(profile)
        return Response(serializer.data, status = status.HTTP_201_CREATED)


class ProfilePageView(APIView):
    def get(self, request, id, format = None):
        profile = Profile.objects.get(external_id = id)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def put(self, request, id, format = None):
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
