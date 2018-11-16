from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import *


class AuthView(APIView):
    def post(self, request, format = None):
        country_code = request.data['country_code']
        number = request.data['number']
        phones = Phone.objects.all()
        is_registred = False
        for phone in phones:
            if country_code == phone.country_code and number == phone.number:
                is_registred = True
                break
        return Response(is_registred, status = status.HTTP_200_OK)
