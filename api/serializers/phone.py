from rest_framework import serializers
from api.models import *


class PhoneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Phone
        fields = ('country_code', 'number')
