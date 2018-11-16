from rest_framework import serializers
from api.models import *
from .phone import PhoneSerializer


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    phone = PhoneSerializer()

    class Meta:
        model = Profile
        fields = ('external_id', 'phone', 'first_name', 'last_name', 'photo', 'status')
