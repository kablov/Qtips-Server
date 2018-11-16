from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import *
from api.serializers import *


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
