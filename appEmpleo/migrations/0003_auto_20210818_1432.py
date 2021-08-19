# Generated by Django 3.1.12 on 2021-08-18 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appEmpleo', '0002_auto_20210702_1426'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solicitud',
            name='servMiliDesde',
        ),
        migrations.RemoveField(
            model_name='solicitud',
            name='servMiliExplicacion',
        ),
        migrations.RemoveField(
            model_name='solicitud',
            name='servMiliHasta',
        ),
        migrations.RemoveField(
            model_name='solicitud',
            name='servMiliRama',
        ),
        migrations.RemoveField(
            model_name='solicitud',
            name='servMiliRango',
        ),
        migrations.RemoveField(
            model_name='solicitud',
            name='servMiliTipo',
        ),
        migrations.AddField(
            model_name='solicitud',
            name='isHizoServMili',
            field=models.BooleanField(db_column='is_hizo_serv_militar', default=False),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='disponibilidad',
            field=models.CharField(choices=[('Part-Time', 'Part-Time'), ('Full-Time', 'Full-Time')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='escSecundaria',
            field=models.CharField(blank=True, db_column='esc_secundaria', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='nss',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='otraEscDireccion',
            field=models.CharField(blank=True, db_column='otra_esc_direccion', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='otraEscuela',
            field=models.CharField(blank=True, db_column='otra_escuela', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='peDosCompania',
            field=models.CharField(blank=True, db_column='pe2_compania', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='peDosDireccion',
            field=models.CharField(blank=True, db_column='pe2_direccion', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='peDosPuesto',
            field=models.CharField(blank=True, db_column='pe2_puesto', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='peDosRazonesIrse',
            field=models.TextField(blank=True, db_column='pe2_razones_irse', null=True),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='peDosResponsabilidades',
            field=models.TextField(blank=True, db_column='pe2_responsabilidades', null=True),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='peDosSupervisor',
            field=models.CharField(blank=True, db_column='pe2_supervisor', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='peDosTelefono',
            field=models.CharField(blank=True, db_column='pe2_telefono', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='peUnoCompania',
            field=models.CharField(blank=True, db_column='pe1_compania', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='peUnoDireccion',
            field=models.CharField(blank=True, db_column='pe1_direccion', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='peUnoPuesto',
            field=models.CharField(blank=True, db_column='pe1_puesto', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='peUnoRazonesIrse',
            field=models.TextField(blank=True, db_column='pe1_razones_irse', null=True),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='peUnoResponsabilidades',
            field=models.TextField(blank=True, db_column='pe1_responsabilidades', null=True),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='peUnoSupervisor',
            field=models.CharField(blank=True, db_column='pe1_supervisor', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='peUnoTelefono',
            field=models.CharField(blank=True, db_column='pe1_telefono', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='refDosCompania',
            field=models.CharField(blank=True, db_column='ref2_compania', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='refDosNombreCompleto',
            field=models.CharField(blank=True, db_column='ref2_nombre_completo', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='refDosRelacion',
            field=models.CharField(blank=True, db_column='ref2_relacion', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='refDosTelefono',
            field=models.CharField(blank=True, db_column='ref2_telefono', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='refUnoCompania',
            field=models.CharField(blank=True, db_column='ref1_compania', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='secDiploma',
            field=models.CharField(blank=True, db_column='sec_diploma', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='secDireccion',
            field=models.CharField(blank=True, db_column='sec_direccion', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='uniDiploma',
            field=models.CharField(blank=True, db_column='uni_diploma', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='uniDireccion',
            field=models.CharField(blank=True, db_column='uni_direccion', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='universidad',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]