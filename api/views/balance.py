from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import *
from qtips.decorators import *
from qtips.permissions import *


class BalanceView(APIView):
    @catch_errors
    def get(self, request, id, format = None):
        access_key_check(request)
        profile = Profile.objects.get(external_id = id)
        is_owner_or_read_only(request, profile)
        transactions = Transaction.objects.filter(to_user = profile)
        profile.balance = sum(transaction.amount for transaction in transactions)
        profile.save(update_fields = ['balance'])
        return Response(profile.balance, status = status.HTTP_200_OK)
