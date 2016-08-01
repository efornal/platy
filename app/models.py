# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
import logging


class Doctype(models.Model):
    id = models.AutoField( primary_key=True,null=False)
    abreviatura = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'doctypes'
        verbose_name = _('Doctype')
        verbose_name_plural = _('Doctypes')

    def __unicode__(self):
        return "%s" % (self.abreviatura)

    
class Institute(models.Model):
    id = models.AutoField( primary_key=True,null=False)
    descripcion = models.TextField( null=True, blank=True )
    nombre_corto = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'institutes'
        verbose_name = _('Institute')
        verbose_name_plural = _('Institutes')

    def __unicode__(self):
        return "%s" % (self.nombre_corto)

    
class Career(models.Model):
    id = models.AutoField( primary_key=True,null=False)
    institute = models.ForeignKey(Institute,models.DO_NOTHING, default=0)
    descripcion = models.TextField( null=True, blank=True )
    
    class Meta:
        managed = False
        db_table = 'careers'
        verbose_name = _('Career')
        verbose_name_plural = _('Careers')

    def __unicode__(self):
        return "%s" % (self.id)


class Order(models.Model):
    id = models.AutoField( primary_key=True,null=False)
    nro_expediente = models.TextField( null=True, blank=True )
    doctype = models.ForeignKey(Doctype, models.DO_NOTHING, blank=True, null=True)
    documento = models.CharField(max_length=10, blank=True, null=True)
    apellido = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    career = models.ForeignKey(Career, models.DO_NOTHING, default=0)
    registro_facultad = models.CharField(max_length=50)
    registro_universidad = models.CharField(max_length=50)
    libro = models.IntegerField(blank=True, null=True)
    pagina = models.IntegerField(blank=True, null=True)
    tomo = models.IntegerField()
    fecha_ultimo_examen = models.DateField(blank=True, null=True)
    fecha_entrada = models.DateField(blank=True, null=True)
    fecha_pase_imprenta = models.DateField(blank=True, null=True)
    fecha_expedicion = models.DateField()
    nro_resolucion = models.CharField(max_length=150, blank=True, null=True)
    fecha_pase_facultad = models.DateField(blank=True, null=True)
    nro_envio = models.TextField( null=True, blank=True )
    fecha_regreso = models.DateField(blank=True, null=True)
    fecha_devolucion = models.DateField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    apellido_canonico = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'orders'
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

    def __unicode__(self):
        return "%s" % (self.id)

    
class User(models.Model):
    id = models.AutoField( primary_key=True,null=False)
    doctype = models.ForeignKey(Doctype, models.DO_NOTHING, blank=True, null=True)
    documento = models.IntegerField()
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=50)
    usuario = models.CharField(unique=True, max_length=15)
    hashed_password = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'users'
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __unicode__(self):
        return "%s" % (self.id)
