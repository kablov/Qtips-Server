from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Profile, Transaction
from django.shortcuts import render
from qtips import settings


def payment_page(request, id):
    return render(request, 'tip_payment.html', {})


class TipPaymentView(APIView):
    def post(self, request, id, format = None):
        profile = Profile.objects.get(external_id = id)
        amount = request.data['amount']
        transaction = Transaction()
        transaction.to_user = profile
        transaction.type = 'tip_payment'
        transaction.amount = amount
        transaction.save()
        return render(request, 'successful_payment.html', {})
