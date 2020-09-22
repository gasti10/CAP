# Generated by Django 3.1.1 on 2020-09-21 19:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('intranet', '0002_auto_20200921_1250'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='formulario',
            options={'ordering': ['-id'], 'verbose_name': 'Cliente', 'verbose_name_plural': 'Formularios'},
        ),
        migrations.AddField(
            model_name='formulario',
            name='permiso',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='pais',
            field=models.CharField(choices=[('1', 'Argentina'), ('2', 'Chile'), ('3', 'Uruguay'), ('4', 'Bolivia')], default='Argentina', help_text='(agregue opciones para evitar posibles errores en el tipeo, faltaría agregar los paises que correspondan)', max_length=200, verbose_name='Pais'),
        ),
    ]
