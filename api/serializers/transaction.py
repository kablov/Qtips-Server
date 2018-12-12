from rest_framework import serializers
from api.models import Transaction


class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transaction
        fields = ('id', 'amount', 'time', 'type')
