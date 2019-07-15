from django.shortcuts import render, redirect
from rest_framework.views import APIView
from api.models import Profile, Transaction


def payment_page(request, id):
    profile = Profile.objects.get(external_id=id)
    return render(request, 'payment/Index.html', {"profile": profile})

class TipPaymentView(APIView):
    def post(self, request, id, format=None):
        profile = Profile.objects.get(external_id=id)
        amount = request.data['amount']
        transaction = Transaction()
        transaction.recipient = profile
        transaction.type = 'tip_payment'
        transaction.amount = amount
        transaction.save()

        try:
            devices = profile.fcm_devices.all()
            devices.send_message(title="Поступили чаевые", body="Вам отправили чаевые в размере " + str(amount) + " рублей.",
                                 sound='cash.wav', content_available=True, data={"category": "NEW_TIPS"})
        finally:
            link = 'http://' + request.META['HTTP_HOST'] + '/thanks'
            return redirect(link)


def test_payment_page(request):
    profile = Profile.objects.get(external_id=404490)
    return render(request, 'payment/Index.html', {"profile": profile})

class TestTipPaymentView(APIView):
    def post(self, request, format=None):
        profile = Profile.objects.get(external_id=404490)
        amount = request.data['amount']
        transaction = Transaction()
        transaction.recipient = profile
        transaction.type = 'tip_payment'
        transaction.amount = amount
        transaction.save()

        try:
            devices = profile.fcm_devices.all()
            devices.send_message(message={"title": "Поступили чаевые", "body": "Вам отправили чаевые в размере " + str(amount) + " рублей."},
                                 extra={"category": "TIP_PAYMENT"})
        finally:
            link = 'http://' + request.META['HTTP_HOST'] + '/thanks'
            return redirect(link)
