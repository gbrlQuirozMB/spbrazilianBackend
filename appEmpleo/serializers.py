from rest_framework import serializers

from .models import *


class SolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitud
        fields = '__all__'


class SolicitudAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitud
        fields = ['id', 'isRevisado', 'comentariosRespuestas']
