from appEmpleo.models import *

from django.test import TestCase
from rest_framework.test import APITestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User
import json
from rest_framework import status


def configDB():
    Solicitud.objects.create(posicionDeseada='Administrative', nombreCompleto='nombreCompleto1', fechaNac='2021-04-06', calle='calle1', numInterior='numImt1', ciudad='ciudad1', estado='estado1',
                             cp='cp1', telefono='telefono1', email='email1', nss='nss1', disponibilidad='disponibilidad1', escSecundaria='escSecundaria1', secDireccion='secDireccion1',
                             universidad='universidad1', uniDireccion='uniDireccion1', refUnoNombreCompleto='refUnoNombreCompleto1', refUnoRelacion='refUnoRelacion1',
                             refUnoCompania='refUnoCompania1', refUnoTelefono='refUnoTelefono1', refDosNombreCompleto='refDosNombreCompleto1', refDosRelacion='refDosRelacion1',
                             refDosCompania='refDosCompania1', refDosTelefono='refDosTelefono', peUnoCompania='peUnoCompania1', peUnoTelefono='peUnoTelefono1', peUnoDireccion='peUnoDireccion1',
                             peUnoSupervisor='peUnoSupervisor1', peUnoPuesto='peUnoPuesto1', peDosCompania='peDosCompania1', peDosTelefono='peDosTelefono', peDosDireccion='peDosDireccion',
                             peDosSupervisor='peDosSupervisor1', peDosPuesto='peDosPuesto1')
    Solicitud.objects.create(posicionDeseada='Administrative', nombreCompleto='nombreCompleto2', fechaNac='2022-04-06', calle='calle2', numInterior='numImt2', ciudad='ciudad2', estado='estado2',
                             cp='cp2', telefono='telefono2', email='email2', nss='nss2', disponibilidad='disponibilidad2', escSecundaria='escSecundaria2', secDireccion='secDireccion2',
                             universidad='universidad2', uniDireccion='uniDireccion2', refUnoNombreCompleto='refUnoNombreCompleto2', refUnoRelacion='refUnoRelacion2',
                             refUnoCompania='refUnoCompania2', refUnoTelefono='refUnoTelefono2', refDosNombreCompleto='refDosNombreCompleto2', refDosRelacion='refDosRelacion2',
                             refDosCompania='refDosCompania2', refDosTelefono='refDosTelefono', peUnoCompania='peUnoCompania2', peUnoTelefono='peUnoTelefono2', peUnoDireccion='peUnoDireccion2',
                             peUnoSupervisor='peUnoSupervisor2', peUnoPuesto='peUnoPuesto2', peDosCompania='peDosCompania2', peDosTelefono='peDosTelefono', peDosDireccion='peDosDireccion',
                             peDosSupervisor='peDosSupervisor2', peDosPuesto='peDosPuesto2')
    Solicitud.objects.create(posicionDeseada='Administrative', nombreCompleto='nombreCompleto3', fechaNac='3033-04-06', calle='calle3', numInterior='numImt3', ciudad='ciudad3', estado='estado3',
                             cp='cp3', telefono='telefono3', email='email3', nss='nss3', disponibilidad='disponibilidad3', escSecundaria='escSecundaria3', secDireccion='secDireccion3',
                             universidad='universidad3', uniDireccion='uniDireccion3', refUnoNombreCompleto='refUnoNombreCompleto3', refUnoRelacion='refUnoRelacion3',
                             refUnoCompania='refUnoCompania3', refUnoTelefono='refUnoTelefono3', refDosNombreCompleto='refDosNombreCompleto3', refDosRelacion='refDosRelacion3',
                             refDosCompania='refDosCompania3', refDosTelefono='refDosTelefono', peUnoCompania='peUnoCompania3', peUnoTelefono='peUnoTelefono3', peUnoDireccion='peUnoDireccion3',
                             peUnoSupervisor='peUnoSupervisor3', peUnoPuesto='peUnoPuesto3', peDosCompania='peDosCompania3', peDosTelefono='peDosTelefono', peDosDireccion='peDosDireccion',
                             peDosSupervisor='peDosSupervisor3', peDosPuesto='peDosPuesto3')


# python manage.py test --settings=server.settings.dev appEmpleo.tests.PostSolicitudTest
class PostSolicitudTest(APITestCase):
    def setUp(self):
        self.json = {
            "posicionDeseada": "Administrative",
            "nombreCompleto": "Gabriel Quiroz Olvera",
            "fechaNac": "2021-04-06",
            "calle": "Av. de los Desarrolladores de Python",
            "numInterior": "369-F",
            "ciudad": "Pachuca de Soto",
            "estado": "Hidalgo",
            "cp": "42083",
            "telefono": "7711896184",
            "email": "gabriel@mb.company",
            "nss": "123-456-789",
            "martes": True,
            "sabado": True,
            "turnoVespertino": True,
            "disponibilidad": "Full-Time",
            "isCiudadano": False,

            "isTrabajadoAntes": True,
            "cuando": "2021-01-01",

            "isExconvicto": True,
            "explicacion": "me robe un pan, porque no tenia dinero para comer",

            "escSecundaria": "Escuela Secundaria Tecnica No. 1",
            "secDireccion": "Blvb. Felipe Angeles S/N",
            "secIsGraduado": True,
            "secDiploma": "Tecnico en Electricidad",

            "universidad": "Universidad Autonoma del Estado de Hidalgo",
            "uniDireccion": "Carr. Pachuca-Tulancingo, km. 4.5, Col. Carboneras, Mineral de la Reforma ",
            "uniIsGraduado": True,
            "uniDiploma": "Lic. en Computacion",

            "refUnoNombreCompleto": "Elianid Tolentino Cabrera",
            "refUnoRelacion": "Jefa de la cocina",
            "refUnoCompania": "Personal",
            "refUnoTelefono": "7711896185",

            "refDosNombreCompleto": "Laura Grissel Cabrera Bejarano",
            "refDosRelacion": "Jefa de la casa",
            "refDosCompania": "Desconozco donde era",
            "refDosTelefono": "771896186",

            "peUnoCompania": "Auditoria Superior del Estado de Hidalgo",
            "peUnoTelefono": "771896187",
            "peUnoDireccion": "Av. Tecnologico 201, Puerta de Hierro, 42086 Pachuca de Soto, Hgo.",
            "peUnoSupervisor": "Director de Informatica",
            "peUnoPuesto": "SubDirector de Informatica",

            "peDosCompania": "Secretaria de Contraloria",
            "peDosTelefono": "771189619",
            "peDosDireccion": "Camino Real de la Plata # 301, tercer piso Fracc. Zona Plateada, C.P. 42084",
            "peDosSupervisor": "Adminstrador General",
            "peDosPuesto": "Encargado de Departamento"
        }

    def test(self):
        response = self.client.post('/api/empleo/solicitud/create/', data=json.dumps(self.json), content_type='application/json')
        print(f'response JSON ===>>> OK \n {json.dumps(response.json())} \n --- \n')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Solicitud.objects.get(id=1).nombreCompleto, 'Gabriel Quiroz Olvera')
        self.assertEqual(Solicitud.objects.filter().count(), 1)

        # del self.json['cuando']
        self.json['cuando'] = None
        response = self.client.post('/api/empleo/solicitud/create/', data=json.dumps(self.json), content_type='application/json')
        print(f'response JSON ===>>> 409 si ha trabajado antes, debe decir cuando \n {json.dumps(response.json())} \n --- \n')
        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)

        self.json['cuando'] = '2021-01-01'
        del self.json['explicacion']
        response = self.client.post('/api/empleo/solicitud/create/', data=json.dumps(self.json), content_type='application/json')
        print(f'response JSON ===>>> 409 si es exconvicto, debe explicar\n {json.dumps(response.json())} \n --- \n')
        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)

        self.json['explicacion'] = 'me robe un pan, porque no tenia dinero para comer'
        del self.json['secDiploma']
        response = self.client.post('/api/empleo/solicitud/create/', data=json.dumps(self.json), content_type='application/json')
        print(f'response JSON ===>>> 409 si es graduado, debe indicar diploma\n {json.dumps(response.json())} \n --- \n')
        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)

        self.json['secDiploma'] = 'Tecnico en Electricidad'
        del self.json['uniDiploma']
        response = self.client.post('/api/empleo/solicitud/create/', data=json.dumps(self.json), content_type='application/json')
        print(f'response JSON ===>>> 409 si es graduado, debe indicar diploma\n {json.dumps(response.json())} \n --- \n')
        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)

        self.json.pop('nombreCompleto', None)
        del self.json['nss']
        del self.json['email']
        response = self.client.post('/api/empleo/solicitud/create/', data=json.dumps(self.json), content_type='application/json')
        print(f'response JSON ===>>> 400 faltan 3 campos \n {json.dumps(response.json())} \n --- \n')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


# python manage.py test --settings=server.settings.dev appEmpleo.tests.GetSolicitudDetailTest
class GetSolicitudDetailTest(APITestCase):
    def setUp(self):
        configDB()

        self.user = User.objects.create_user(username='gabriel', is_staff=True)  # IsAuthenticated

    def test(self):
        response = self.client.get('/api/empleo/solicitud/3/detail/')
        print(f'\n response JSON ===>>> 401 no autorizado \n {json.dumps(response.json())} \n ---')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.client.force_authenticate(user=self.user)

        response = self.client.get('/api/empleo/solicitud/3/detail/')
        print(f'\n response JSON ===>>> ok (3) \n {json.dumps(response.json())} \n ---')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.get('/api/empleo/solicitud/33/detail/')
        print(f'\n response JSON ===>>> 404 \n {json.dumps(response.json())} \n ---')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


# python manage.py test --settings=server.settings.dev appEmpleo.tests.PutSolicitudAdminTest
class PutSolicitudAdminTest(APITestCase):
    def setUp(self):
        configDB()

        self.json = {
            "isRevisado": True,
            "comentariosRespuestas": "ES UN MUY BUEN CANDIDATO"
        }

        self.user = User.objects.create_user(username='gabriel', is_staff=True)  # IsAuthenticated

    def test(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.put('/api/empleo/solicitud-admin/3/update/', data=json.dumps(self.json), content_type='application/json')
        print(f'\n response JSON ===>>> ok (3) \n {json.dumps(response.json())} \n ---')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Solicitud.objects.get(id=3).isRevisado)
        self.assertEqual(Solicitud.objects.get(id=3).comentariosRespuestas, 'ES UN MUY BUEN CANDIDATO')

        response = self.client.put('/api/empleo/solicitud-admin/33/update/', data=json.dumps(self.json), content_type='application/json')
        print(f'\n response JSON ===>>> 404 \n {json.dumps(response.json())} \n ---')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
