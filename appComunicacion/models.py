from django.db import models


class DatosCorreo(models.Model):
    creado_en = models.DateTimeField(auto_now_add=True)
    nombre = models.CharField(default='Ninguno', max_length=200)
    email = models.CharField(default='Ninguno', max_length=100)
    telefono = models.CharField(default='Ninguno', max_length=15)
    mensaje = models.TextField(default='')
    # administrativos
    isAtendido = models.BooleanField(default=False)
    respuesta = models.TextField(default='')

    class Meta:
        db_table = 'datos_correo'
        ordering = ['-id']
