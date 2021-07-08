from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework import permissions

from api.exceptions import *
from .serializers import *
import logging
log = logging.getLogger('django')

from django.core.mail import send_mail


class EnviarCorreoCreateView(CreateAPIView):
    serializer_class = DatosCorreoSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = DatosCorreoSerializer(data=request.data)
        if serializer.is_valid():
            try:
                nombre = request.data.get('nombre')
                email = request.data.get('email')
                telefono = request.data.get('telefono')
                mensaje = request.data.get('mensaje')
                nl = '\n'
                text_content = f'Hi,{nl}{nl} The client: {nombre}. {nl} Says: {mensaje}. {nl} Contact data: {nl} \t Phone: {telefono} {nl} \t Email: {email}'
                send_mail(
                    'SP Brazilian - Contact Us',
                    text_content,
                    'no-reply@spbrazilian.com',
                    ['info@spbrazilian.com'],
                    fail_silently=False,
                )
            except:
                raise ResponseError(f'Error al enviar correo', 500)

            return self.create(request, *args, **kwargs)
        log.error(f'campos incorrectos: {serializer.errors}')
        raise ResponseBadRequest(serializer.errors)
