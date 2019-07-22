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
        transaction = Transaction()
        transaction.recipient = profile
        transaction.type = 'withdraw'
        transaction.amount = amount
        transaction.save()
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
        withdraw_request = WithdrawRequest()
        withdraw_request.profile = profile
        withdraw_request.amount = amount
        withdraw_request.save()
        return Response("Заявка на снятие средств отправлена",
                        status=status.HTTP_201_CREATED)


class WithdrawRequestsView(APIView):
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
