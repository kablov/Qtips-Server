from rest_framework import serializers
from api.models import *


class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transaction
        fields = ('amount', 'time', 'type')
