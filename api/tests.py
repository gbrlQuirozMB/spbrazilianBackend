from django.test import TestCase
from rest_framework.test import APITestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User
import json
from rest_framework import status


def configDB():
    User.objects.create_user(username='limitado', email='limitado@spbrazilian.com', password='password', first_name='Juanito', last_name='Perez')
    User.objects.create_user(username='admin', email='gabriel@mb.company', password='sepalaching', first_name='Gabriel', last_name='Quiroz', is_superuser=True)
    User.objects.create_user(username='admin_spb', email='admin@spbrazilian.com', password='AJXU67W7Fx', first_name='Panchito', last_name='Sanchez', is_staff=True)


# python manage.py test api.tests.LoginTest --settings=server.settings.dev
class LoginTest(APITestCase):
    def setUp(self):

        configDB()

        self.json = {
            "username": "admin_spb",
            "password": "AJXU67W7Fx"
        }

    def test(self):
        response = self.client.post('/api/login/', data=json.dumps(self.json), content_type='application/json')
        print(f'response JSON ===>>> OK \n {json.dumps(response.json())} \n --- \n')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        print(f'otra prueba sin respuesta')
        self.assertTrue(self.client.login(username='admin_spb', password='AJXU67W7Fx'))
