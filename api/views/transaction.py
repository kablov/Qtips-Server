from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Profile, Token, Transaction
from api.serializers import TransactionSerializer
from qtips.decorators import catch_errors
from qtips.permissions import access_key_check


class TransactionHistoryView(APIView):
    @catch_errors
    def get(self, request, format = None):
        access_key_check(request)
        token = Token.objects.get(token = request.META.get('HTTP_AUTHORIZATION')[6:])
        profile = Profile.objects.get(token = token)
        transactions = Transaction.objects.filter(recipient = profile).order_by('-time')
        serializer = TransactionSerializer(transactions, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
