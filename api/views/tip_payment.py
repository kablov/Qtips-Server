from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import *


class TipPaymentView(APIView):
    def post(self, request, id, format = None):
        profile = Profile.objects.get(external_id = id)
        sum = request.data['sum']
        transaction = Transaction()
        transaction.to_user = profile
        transaction.type = 'tip_payment'
        transaction.amount = sum
        transaction.save()

        profile.balance += int(sum)
        profile.save(update_fields = ['balance'])
        return Response(status = status.HTTP_201_CREATED)
