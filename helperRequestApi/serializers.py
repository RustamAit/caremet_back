from rest_framework import serializers

from helperRequestApi.models import *


class HelperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Helper
        fields = '__all__'


class HelperRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelperRequest
        fields = '__all__'
