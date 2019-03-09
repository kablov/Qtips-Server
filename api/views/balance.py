from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Profile, Token, Transaction
from qtips.decorators import catch_errors
from qtips.permissions import access_key_check


class BalanceView(APIView):
    @catch_errors
    def get(self, request, format = None):
        access_key_check(request)
        token = Token.objects.get(token = request.META.get('HTTP_AUTHORIZATION')[6:])
        profile = Profile.objects.get(token = token)
        transactions = Transaction.objects.filter(recipient = profile)
        profile.balance = sum(transaction.amount for transaction in transactions)
        profile.save(update_fields = ['balance'])
        return Response(profile.balance, status = status.HTTP_200_OK)
