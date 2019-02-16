from rest_framework import serializers
from api.models import Profile
from .phone import PhoneSerializer


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    phone = PhoneSerializer()
    id = serializers.IntegerField(source = 'external_id')

    class Meta:
        model = Profile
        fields = ('id', 'phone', 'first_name', 'last_name', 'email', 'photo', 'balance', 'qr', 'payment_url', 'status')
