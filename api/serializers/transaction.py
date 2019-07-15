from rest_framework import serializers
from api.models import Transaction


class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    time = serializers.DateTimeField(format=("%Y-%m-%dT%H:%M:%S.%f%z"))

    class Meta:
        model = Transaction
        fields = ('id', 'amount', 'time', 'type')
