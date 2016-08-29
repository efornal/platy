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
    abreviatura = models.CharField(max_length=4,  null=False,
                                   verbose_name=_('abbreviation'))

    class Meta:
        db_table = 'doctypes'
        verbose_name = _('Doctype')
        verbose_name_plural = _('Doctypes')

    def __unicode__(self):
        return "%s" % (self.abreviatura)

    
class Institute(models.Model):
    id = models.AutoField( primary_key=True,null=False)
    descripcion = models.TextField( null=False,
                                   verbose_name=_('description') )
    nombre_corto = models.CharField(max_length=8,
                                   verbose_name=_('short_name'))

    class Meta:
        db_table = 'institutes'
        verbose_name = _('Institute')
        verbose_name_plural = _('Institutes')

    def __unicode__(self):
        return "%s" % (self.nombre_corto)

    
class Career(models.Model):
    id = models.AutoField( primary_key=True,null=False)
    institute = models.ForeignKey(Institute,models.DO_NOTHING, default=0,
                                   verbose_name=_('institute'))
    descripcion = models.TextField( null=False,
                                   verbose_name=_('description'))
    
    class Meta:
        db_table = 'careers'
        verbose_name = _('Career')
        verbose_name_plural = _('Careers')

    def __unicode__(self):
        return "%s" % (self.descripcion)

    institute.short_description = _("institute")


class Order(models.Model):
    id = models.AutoField( primary_key=True,null=False)
    nro_expediente = models.TextField( null=False,
                                   verbose_name=_('expedient_number'))
    doctype = models.ForeignKey(Doctype, models.DO_NOTHING, null=False,
                                   verbose_name=_('document_type'))
    documento = models.CharField(max_length=10, null=False,
                                   verbose_name=_('document_number'))
    apellido = models.CharField(max_length=50, null=False,
                                   verbose_name=_('surname'))
    nombre = models.CharField(max_length=50, null=False,
                                   verbose_name=_('name'))
    career = models.ForeignKey(Career, models.DO_NOTHING, default=0,
                                   verbose_name=_('career'))
    registro_facultad = models.CharField(max_length=50,
                                   verbose_name=_('faculty_registration'))
    registro_universidad = models.CharField(max_length=50,
                                   verbose_name=_('university_registration'))
    libro = models.IntegerField(blank=True, null=True,
                                   verbose_name=_('book'))
    pagina = models.IntegerField(blank=True, null=True,
                                   verbose_name=_('page'))
    tomo = models.IntegerField(blank=True, null=True,
                               verbose_name=_('volume'))
    fecha_ultimo_examen = models.DateField(blank=True, null=True,
                                   verbose_name=_('last_exam_date'))
    fecha_entrada = models.DateField(blank=True, null=True,
                                   verbose_name=_('entry_date'))
    fecha_pase_imprenta = models.DateField(blank=True, null=True,
                                   verbose_name=_('printing_pass_date'))
    fecha_expedicion = models.DateField(blank=True, null=True,
                                        verbose_name=_('expedition_date'))
    nro_resolucion = models.CharField(max_length=150, blank=True, null=True,
                                   verbose_name=_('resolution_number'))
    fecha_pase_facultad = models.DateField(blank=True, null=True,
                                   verbose_name=_('faculty_pass_date'))
    nro_envio = models.TextField( null=True, blank=True,
                                   verbose_name=_('delivery_number'))
    fecha_regreso = models.DateField(blank=True, null=True,
                                   verbose_name=_('return_date'))
    fecha_devolucion = models.DateField(blank=True, null=True,
                                   verbose_name=_('devolution_date'))
    observaciones = models.TextField(blank=True, null=True,
                                   verbose_name=_('observations'))
    apellido_canonico = models.CharField(max_length=50, blank=True, null=True,
                                   verbose_name=_('canonical_name'))

    class Meta:
        db_table = 'orders'
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

    def __unicode__(self):
        return "%s" % (self.nro_expediente)

    def surname_and_name(self):
        return "%s, %s" % (self.apellido, self.nombre)
    surname_and_name.short_description= _('surname_and_name')

    def institute_description(self):
        return "%s" % self.career.institute.descripcion
    institute_description.short_description= _('institute_description')

    def institute_short_name(self):
        return "%s" % self.career.institute.nombre_corto
    institute_short_name.short_description= _('institute_short_name')

