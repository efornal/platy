from django.contrib import admin
from app.models import Institute
from app.models import Doctype
from app.models import Career
from app.models import Order
from app.models import User
from django.conf.locale.es import formats as es_formats

es_formats.DATETIME_FORMAT = "d-m-Y H:i"


class DoctypeAdmin(admin.ModelAdmin):
    list_display = ('abreviatura',)
    search_fields = ['abreviatura']
    ordering = ('abreviatura',)


class CareerAdmin(admin.ModelAdmin):
    list_display = ('descripcion','institute')
    search_fields = ['descripcion']
    ordering = ('descripcion',)


class InstituteAdmin(admin.ModelAdmin):
    list_display = ('descripcion','nombre_corto')
    search_fields = ['descripcion', 'nombre_corto']
    ordering = ('descripcion',)

    
class OrderAdmin(admin.ModelAdmin):
    list_display = ('surname_and_name','documento','nro_expediente'
                    ,'institute_short_name','career')
    search_fields = ['documento', 'nombre', 'apellido']
    ordering = ('apellido','nombre', 'documento')

    
# # Register your models here.
admin.site.register(Institute, InstituteAdmin)
admin.site.register(Doctype, DoctypeAdmin)
admin.site.register(Career, CareerAdmin)
admin.site.register(Order, OrderAdmin)

