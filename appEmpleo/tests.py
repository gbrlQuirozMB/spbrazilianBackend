from appEmpleo.models import *

from django.test import TestCase
from rest_framework.test import APITestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User
import json
from rest_framework import status


def configDB():
    pass

# python manage.py test appEmpleo.tests.PostSolicitudTest --settings=server.settings.dev


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

        del self.json['cuando']
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
