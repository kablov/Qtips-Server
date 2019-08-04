from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from qtips.decorators import catch_errors
from qtips.permissions import access_key_check
from api.serializers import WithdrawRequestSerializer
from api.models import Profile, Token, Transaction, WithdrawRequest


class WithdrawView(APIView):
    @catch_errors
    def post(self, request, format=None):
        access_key_check(request)
        token = Token.objects.get(
            token=request.META.get('HTTP_AUTHORIZATION')[6:]
        )
        profile = Profile.objects.get(token=token)
        amount = request.data['amount']
        Transaction.objects.create(
            recipient=profile,
            type='withdraw',
            amount=amount
        )
        return Response("Заявка на снятие средств отправлена",
                        status=status.HTTP_201_CREATED)


class WithdrawRequestView(APIView):
    @catch_errors
    def post(self, request, format=None):
        access_key_check(request)
        token = Token.objects.get(
            token=request.META.get('HTTP_AUTHORIZATION')[6:]
        )
        profile = Profile.objects.get(token=token)
        amount = request.data['amount']
        WithdrawRequest.objects.create(
            profile=profile,
            amount=amount
        )
        return Response("Заявка на снятие средств отправлена",
                        status=status.HTTP_201_CREATED)


class WithdrawRequestHistoryView(APIView):
    @catch_errors
    def get(self, request, format=None):
        access_key_check(request)
        token = Token.objects.get(
            token=request.META.get('HTTP_AUTHORIZATION')[6:]
        )
        profile = Profile.objects.get(token=token)
        withdraw_requests = WithdrawRequest.objects.filter(
            profile=profile
        ).order_by('-request_date')
        serializer = WithdrawRequestSerializer(withdraw_requests, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
