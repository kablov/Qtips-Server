from django.shortcuts import render, redirect
from rest_framework.views import APIView
from api.models import Profile, Transaction


class TipPaymentView(APIView):
    def get(self, request, id, format=None):
        profile = Profile.objects.get(external_id=id)
        return render(request, 'payment/Index.html', {"profile": profile})

    def post(self, request, id, format=None):
        profile = Profile.objects.get(external_id=id)
        amount = request.data['amount']
        if float(amount) > 50 and float(amount) < 100000:
            transaction = Transaction.objects.create(
                recipient=profile,
                amount=amount
            )
            try:
                devices = transaction.recipient.fcm_devices.all()
                devices.send_message(
                    title="Поступили чаевые",
                    body="Вам отправили чаевые в размере "
                         + str(amount) + " рублей.",
                    sound='cash.wav',
                    content_available=True,
                    data={"category": "NEW_TIPS"}
                )
            finally:
                return redirect('/thanks/')
        else:
            return render(request, 'payment/Index.html', {"profile": profile})


class TestTipPaymentView(APIView):
    def get(self, request, format=None):
        profile = Profile.objects.get(external_id=538660)
        return render(request, 'payment/Index.html', {"profile": profile})

    def post(self, request, format=None):
        profile = Profile.objects.get(external_id=538660)
        amount = request.data['amount']
        if float(amount) > 50 and float(amount) < 100000:
            transaction = Transaction.objects.create(
                recipient=profile,
                amount=amount
            )
            try:
                devices = transaction.recipient.fcm_devices.all()
                devices.send_message(
                    title="Поступили чаевые",
                    body="Вам отправили чаевые в размере "
                         + str(amount) + " рублей.",
                    sound='cash.wav',
                    content_available=True,
                    data={"category": "NEW_TIPS"}
                )
            finally:
                return redirect('/thanks/')
        else:
            return render(request, 'payment/Index.html', {"profile": profile})
