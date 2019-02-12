from rest_framework import serializers
from api.models import WithdrawRequest
from api.serializers import ProfileSerializer


class WithdrawRequestSerializer(serializers.HyperlinkedModelSerializer):
    profile = ProfileSerializer()
    class Meta:
        model = WithdrawRequest
        fields = ('id', 'profile', 'amount', 'request_date', 'status', 'reviewed_time')
