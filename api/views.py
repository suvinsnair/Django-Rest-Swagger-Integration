# api/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .models import AcConfig
from .serializers import AcConfigurationSerializer, \
    AcConfigurationSetHumiditySerializer, \
    AcConfigurationGetHumiditySerializer
from django.forms.models import model_to_dict


class AcConfigurationList(generics.ListCreateAPIView):

    queryset = AcConfig.objects.all()
    serializer_class = AcConfigurationSerializer

    def post(self, request, *args, **kwargs):
        try:
            instance = AcConfig.objects.get()
        except Exception as e:
            instance = AcConfig()
        instance.name = request.data.get('name')
        instance.target_temp = request.data.get('target_temp')
        instance.target_humidity = request.data.get('target_humidity')
        serializer = self.get_serializer(data=model_to_dict(instance))
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)


class AcConfigurationSetHumidity(generics.UpdateAPIView):

    queryset = AcConfig.objects.all()
    serializer_class = AcConfigurationSetHumiditySerializer

    def update(self, request, *args, **kwargs):
        instance = AcConfig.objects.get()
        instance.target_humidity = request.data.get('target_humidity')

        serializer = self.get_serializer(data=model_to_dict(instance))
        serializer.is_valid(raise_exception=True)
        instance.save()

        return Response(serializer.data)


class AcConfigurationGetHumidity(APIView):

    def get(self, request, *args, **kwargs):

        instance = AcConfig.objects.get()

        return Response({'message': 'The Current Humidity is '
                        + str(instance.target_humidity) + '%'})
