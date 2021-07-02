from django.db import models


class Solicitud(models.Model):
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)
    
    posicionDeseada = models.CharField(max_length=25, db_column='posicion_deseada', choices=(
        ('Server/Churrasqueiro', 'Server/Churrasqueiro'),
        ('Bartender', 'Bartender'),
        ('Prep/Line Cook', 'Prep/Line Cook'),
        ('Administrative', 'Administrative'),
        ('Server Assistant', 'Server Assistant'),
        ('Hostess/Cashier', 'Hostess/Cashier'),
        ('Dishwasher', 'Dishwasher'),
    ))
    # applicant information
    nombreCompleto = models.CharField(max_length=200, db_column='nombre_completo')
    fechaNac = models.DateField(db_column='fecha_nacimiento')
    calle = models.CharField(max_length=100)
    numInterior = models.CharField(max_length=10, db_column='num_interior')
    ciudad = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    cp = models.CharField(max_length=15)
    telefono = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    nss = models.CharField(max_length=15)
    salarioDeseado = models.DecimalField(max_digits=8, decimal_places=2, default=0, db_column='salario_deseado')
    lunes = models.BooleanField(default=False)
    martes = models.BooleanField(default=False)
    miercoles = models.BooleanField(default=False)
    jueves = models.BooleanField(default=False)
    viernes = models.BooleanField(default=False)
    sabado = models.BooleanField(default=False)
    domingo = models.BooleanField(default=False)
    turnoMatutino = models.BooleanField(default=False, db_column='turno_matutino')
    turnoVespertino = models.BooleanField(default=False, db_column='turno_vespertino')
    turnoFinesSemana = models.BooleanField(default=False, db_column='turno_fines_semana')
    turnoFeriado = models.BooleanField(default=False, db_column='turno_feriado')
    disponibilidad = models.CharField(max_length=10, choices=(
        ('Part-Time', 'Part-Time'),
        ('Full-Time', 'Full-Time'),
    ))
    isCiudadano = models.BooleanField(default=False, db_column='is_ciudadano')
    isAutorizadoTrabajar = models.BooleanField(default=False, db_column='is_autorizado_trabajar')
    isTrabajadoAntes = models.BooleanField(default=False, db_column='is_trabajado_antes')
    cuando = models.DateField(null=True)
    isExconvicto = models.BooleanField(default=False, db_column='is_exconvicto')
    explicacion = models.TextField(blank=True)
    # education
    escSecundaria = models.CharField(max_length=200, db_column='esc_secundaria')
    secDireccion = models.CharField(max_length=200, db_column='sec_direccion')
    secDesde = models.DateField(null=True, db_column='sec_desde')
    secHasta = models.DateField(null=True, db_column='sec_hasta')
    secIsGraduado = models.BooleanField(default=False, db_column='sec_is_graduado')
    secDiploma = models.CharField(blank=True, max_length=100, db_column='sec_diploma')

    universidad = models.CharField(max_length=200)
    uniDireccion = models.CharField(max_length=200, db_column='uni_direccion')
    uniDesde = models.DateField(null=True, db_column='uni_desde')
    unihasta = models.DateField(null=True, db_column='uni_hasta')
    uniIsGraduado = models.BooleanField(default=False, db_column='uni_is_graduado')
    uniDiploma = models.CharField(blank=True, max_length=100, db_column='uni_diploma')

    otraEscuela = models.CharField(blank=True, max_length=200, db_column='otra_escuela')
    otraEscDireccion = models.CharField(blank=True, max_length=200, db_column='otra_esc_direccion')
    # references
    refUnoNombreCompleto = models.CharField(max_length=200, db_column='ref1_nombre_completo')
    refUnoRelacion = models.CharField(max_length=100, db_column='ref1_relacion')
    refUnoCompania = models.CharField(max_length=100, db_column='ref1_compania')
    refUnoTelefono = models.CharField(max_length=15, db_column='ref1_telefono')

    refDosNombreCompleto = models.CharField(max_length=200, db_column='ref2_nombre_completo')
    refDosRelacion = models.CharField(max_length=100, db_column='ref2_relacion')
    refDosCompania = models.CharField(max_length=100, db_column='ref2_compania')
    refDosTelefono = models.CharField(max_length=15, db_column='ref2_telefono')
    # previous employment
    peUnoCompania = models.CharField(max_length=200, db_column='pe1_compania')
    peUnoTelefono = models.CharField(max_length=15, db_column='pe1_telefono')
    peUnoDireccion = models.CharField(max_length=200, db_column='pe1_direccion')
    peUnoSupervisor = models.CharField(max_length=150, db_column='pe1_supervisor')
    peUnoPuesto = models.CharField(max_length=150, db_column='pe1_puesto')
    peUnoSalarioInicial = models.DecimalField(max_digits=8, decimal_places=2, default=0, db_column='pe1_salario_inicial')
    peUnoSalarioFinal = models.DecimalField(max_digits=8, decimal_places=2, default=0, db_column='pe1_salario_final')
    peUnoResponsabilidades = models.TextField(blank=True, db_column='pe1_responsabilidades')
    peUnoDesde = models.DateField(null=True, db_column='pe1_desde')
    peUnoHasta = models.DateField(null=True, db_column='pe1_hasta')
    peUnoRazonesIrse = models.TextField(blank=True, db_column='pe1_razones_irse')
    peUnoPedirReferencia = models.BooleanField(default=False, db_column='pe1_pedir_referencia')

    peDosCompania = models.CharField(max_length=200, db_column='pe2_compania')
    peDosTelefono = models.CharField(max_length=15, db_column='pe2_telefono')
    peDosDireccion = models.CharField(max_length=200, db_column='pe2_direccion')
    peDosSupervisor = models.CharField(max_length=150, db_column='pe2_supervisor')
    peDosPuesto = models.CharField(max_length=150, db_column='pe2_puesto')
    peDosSalarioInicial = models.DecimalField(max_digits=8, decimal_places=2, default=0, db_column='pe2_salario_inicial')
    peDosSalarioFinal = models.DecimalField(max_digits=8, decimal_places=2, default=0, db_column='pe2_salario_final')
    peDosResponsabilidades = models.TextField(blank=True, db_column='pe2_responsabilidades')
    peDosDesde = models.DateField(null=True, db_column='pe2_desde')
    peDosHasta = models.DateField(null=True, db_column='pe2_hasta')
    peDosRazonesIrse = models.TextField(blank=True, db_column='pe2_razones_irse')
    peDosPedirReferencia = models.BooleanField(default=False, db_column='pe2_pedir_referencia')
    # military service
    servMiliRama = models.CharField(blank=True, max_length=200, db_column='serv_mili_rama')
    servMiliDesde = models.DateField(null=True, db_column='serv_mili_desde')
    servMiliHasta = models.DateField(null=True, db_column='serv_mili_hasta')
    servMiliRango = models.CharField(blank=True, max_length=100, db_column='serv_mili_rango')
    servMiliTipo = models.CharField(blank=True, max_length=100, db_column='serv_mili_tipo')
    servMiliExplicacion = models.CharField(blank=True, max_length=200, db_column='serv_mili_explicacion')
    # administrativos
    isRevisado = models.BooleanField(default=False, db_column='is_revisado')
    comentariosRespuestas = models.TextField(default='', db_column='comentarios_respuestas')

    class Meta:
        db_table = 'solicitudes'
        ordering = ['-id']
