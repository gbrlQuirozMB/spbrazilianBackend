from appComunicacion.models import *

from django.test import TestCase
from rest_framework.test import APITestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User
import json
from rest_framework import status

# Create your tests here.


def configDB():
    DatosCorreo.objects.create(nombre='nombre-1', email='email-1', telefono='telefono-1', mensaje='mensaje-1')
    DatosCorreo.objects.create(nombre='nombre-2', email='email-2', telefono='telefono-2', mensaje='mensaje-2')
    DatosCorreo.objects.create(nombre='nombre-3', email='email-3', telefono='telefono-3', mensaje='mensaje-3')
    DatosCorreo.objects.create(nombre='nombre-4', email='email-4', telefono='telefono-4', mensaje='mensaje-4', isAtendido=True, respuesta='todo OK')


# python manage.py test --settings=server.settings.dev appComunicacion.tests.GetCorreoListTest
class GetCorreoListTest(APITestCase):
    def setUp(self):
        configDB()

        self.user = User.objects.create_user(username='gabriel', is_staff=True)  # IsAuthenticated

    def test(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.get('/api/correo/list/')
        print(f'\n response JSON ===>>> ok (3) \n {json.dumps(response.json())} \n ---')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


# python manage.py test --settings=server.settings.dev appComunicacion.tests.PutCorreoTest
class PutCorreoTest(APITestCase):
    def setUp(self):
        configDB()

        self.json = {
            "isAtendido": True,
            "respuesta": "Si ya lo lei"
        }

        self.user = User.objects.create_user(username='gabriel', is_staff=True)  # IsAuthenticated

    def test(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.put('/api/correo/3/update/', data=json.dumps(self.json), content_type='application/json')
        print(f'\n response JSON ===>>> ok (3) \n {json.dumps(response.json())} \n ---')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(DatosCorreo.objects.get(id=3).isAtendido)
        self.assertEqual(DatosCorreo.objects.get(id=3).respuesta, 'Si ya lo lei')

        response = self.client.put('/api/correo/33/update/', data=json.dumps(self.json), content_type='application/json')
        print(f'\n response JSON ===>>> 404 \n {json.dumps(response.json())} \n ---')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
