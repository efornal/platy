# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-29 12:59
from __future__ import unicode_literals
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_change_meta_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='career',
            options={'verbose_name': 'Carrera', 'verbose_name_plural': 'Carreras'},
        ),
        migrations.AlterModelOptions(
            name='doctype',
            options={'verbose_name': 'Tipo Documento', 'verbose_name_plural': 'Tipos Documentos'},
        ),
        migrations.AlterModelOptions(
            name='institute',
            options={'verbose_name': 'Facultad', 'verbose_name_plural': 'Facultades'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Pedido', 'verbose_name_plural': 'Pedidos'},
        ),
    ]
