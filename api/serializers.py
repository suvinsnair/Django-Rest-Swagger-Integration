# api/serializers.py
from rest_framework import serializers
from .models import AcConfig


class AcConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcConfig
        fields = ('name', 'target_temp', 'target_humidity')


class AcConfigurationSetHumiditySerializer(serializers.ModelSerializer):
    class Meta:
        model = AcConfig
        fields = ('target_humidity',)


class AcConfigurationGetHumiditySerializer(serializers.ModelSerializer):
    class Meta:
        model = AcConfig
        fields = ('target_humidity',)