from rest_framework import serializers

from .models import *


class DatosCorreoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatosCorreo
        fields = '__all__'


class DatosCorreoListSerializer(serializers.ModelSerializer):
    # creado_en = serializers.DateTimeField(format='%Y-%b-%d')
    creado_en = serializers.DateTimeField(format='%Y-%m-%d')

    class Meta:
        model = DatosCorreo
        fields = ['id', 'creado_en', 'nombre', 'email', 'telefono', 'isAtendido', 'mensaje', 'respuesta']


class DatosCorreoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatosCorreo
        fields = ['id', 'isAtendido', 'respuesta']
