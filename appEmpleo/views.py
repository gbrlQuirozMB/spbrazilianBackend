from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework import permissions

from api.exceptions import *
from .serializers import *
import logging
log = logging.getLogger('django')


class SolicitudCreateView(CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = SolicitudSerializer

    def post(self, request, *args, **kwargs):
        serializer = SolicitudSerializer(data=request.data)
        if serializer.is_valid():
            if request.data.get('isTrabajadoAntes'):
                if request.data.get('cuando') is None:
                    raise ResponseError('Si ha trabajado antes, debe decir cuando', 409)
            if request.data.get('isExconvicto'):
                if request.data.get('explicacion') is None:
                    raise ResponseError('Si es exconvicto, debe explicar', 409)
            if request.data.get('secIsGraduado'):
                if request.data.get('secDiploma') is None:
                    raise ResponseError('Si es graduado de escuela secundaria, debe indicar diploma', 409)
            if request.data.get('uniIsGraduado'):
                if request.data.get('uniDiploma') is None:
                    raise ResponseError('Si es graduado de universidad, debe indicar diploma', 409)

            return self.create(request, *args, **kwargs)
        log.error(f'campos incorrectos: {serializer.errors}')
        raise ResponseBadRequest(serializer.errors)


class SolicitudDetailView(RetrieveAPIView):
    queryset = Solicitud.objects.filter()
    serializer_class = SolicitudSerializer


class SolicitudAdminUpdateView(UpdateAPIView):
    queryset = Solicitud.objects.filter()
    serializer_class = SolicitudAdminSerializer
    http_method_names = ['put']