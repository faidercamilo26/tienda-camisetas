from django.contrib import admin

# Register your models here.
from .models.persona import Persona
from .models.tipoPersona import TipoPersona
from .models.camiseta import Camiseta
from .models.camisetaColor import CamisetaColor
from .models.catalogo import Catalogo
from .models.color import Color
from .models.detalleFactura import DetalleFactura
from .models.estampado import Estampado
from .models.factura import Factura


class PersonaAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('nombre','apellido','numero_documento','tipo_documento','correo', 'numeroCelular')
    search_fields = ['nombre','apellido','numero_documento']
    list_filter = ('nombre',)
    
    
admin.site.register(Persona, PersonaAdmin)
admin.site.register(TipoPersona)
admin.site.register(Camiseta)
admin.site.register(CamisetaColor)
admin.site.register(Catalogo)
admin.site.register(Color)
admin.site.register(DetalleFactura)
admin.site.register(Estampado)
admin.site.register(Factura)

