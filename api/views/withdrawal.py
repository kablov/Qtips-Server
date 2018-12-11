from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Profile, Token, Transaction
from django.shortcuts import render
from qtips.decorators import catch_errors
from qtips.permissions import access_key_check


class WithdrawalView(APIView):
    @catch_errors
    def post(self, request, format = None):
        access_key_check(request)
        token = Token.objects.get(token = request.META.get('HTTP_AUTHORIZATION')[6:])
        profile = Profile.objects.get(token = token)
        amount = request.data['amount']
        transaction = Transaction()
        transaction.to_user = profile
        transaction.type = 'withdrawal'
        transaction.amount = amount
        transaction.save()
        return Response("Заявка на снятие средств отправлена", status = status.HTTP_201_CREATED)
