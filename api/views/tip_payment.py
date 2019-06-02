from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Profile, Transaction
from django.shortcuts import render, redirect


def payment_page(request, id):
    return render(request, 'tip_payment.html', {})


class TipPaymentView(APIView):
    def post(self, request, id, format = None):
        profile = Profile.objects.get(external_id = id)
        amount = request.data['amount']
        transaction = Transaction()
        transaction.recipient = profile
        transaction.type = 'tip_payment'
        transaction.amount = amount
        transaction.save()

        try:
            devices = profile.fcm_devices.all()
            devices.send_message(title = "Поступили чаевые", body = "Вам отправили чаевые в размере " + str(amount) + " рублей.", sound = 'cash.wav', content_available = True, data={"category": "NEW_TIPS"})
        finally:
            link = 'http://' + request.META['HTTP_HOST'] + '/thanks'
            return redirect(link)


def test_payment_page(request):
    return render(request, 'tip_payment.html', {})

class TestTipPaymentView(APIView):
    def post(self, request, format = None):
        profile = Profile.objects.get(external_id = 398466)
        amount = request.data['amount']
        transaction = Transaction()
        transaction.recipient = profile
        transaction.type = 'tip_payment'
        transaction.amount = amount
        transaction.save()

        try:
            devices = profile.fcm_devices.all()
            devices.send_message(message = {"title": "Поступили чаевые", "body": "Вам отправили чаевые в размере " + str(amount) + " рублей."},  extra = {"category" : "TIP_PAYMENT"})
        finally:
            return render(request, 'successful_payment.html', {})
