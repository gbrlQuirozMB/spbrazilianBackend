# Generated by Django 3.1.12 on 2021-07-01 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appComunicacion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='datoscorreo',
            name='actualizado_en',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='datoscorreo',
            name='isAtendido',
            field=models.BooleanField(db_column='is_atendido', default=False),
        ),
    ]
