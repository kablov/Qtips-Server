from rest_framework import serializers
from api.models import *


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('external_id', 'phone', 'first_name', 'last_name', 'photo' 'status')
