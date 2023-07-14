from django.contrib import admin
from .models import *
# Register your models here.

class ArtistaAdmin(admin.ModelAdmin):
    list_display = ['rut','nombre','tipo']
    list_editable = ['nombre']
    search_fields = ['rut']
    list_filter = ['tipo']
    
class TipoAdmin(admin.ModelAdmin):
    list_filter = ['nombre']

class TipoObra(admin.ModelAdmin):
    list_filter = ['nombre']    
    
admin.site.register(Tipo, TipoAdmin)
admin.site.register(Artista, ArtistaAdmin)
admin.site.register(Obra)
admin.site.register(Contacto)
