from rest_framework import serializers
from api.models import Transaction


class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transaction
        fields = ('amount', 'time', 'type')
