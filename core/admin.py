from django.contrib import admin
from .models import user
from .models.tipoPersona import TipoPersona
from .models.camiseta import Camiseta
from .models.camisetaColor import CamisetaColor
#from .models.catalogo import Catalogo
from .models.color import Color
from .models.detalleFactura import DetalleFactura
#from .models.estampado import Estampado
from .models.factura import Factura
from django.contrib.auth import get_user_model
User = get_user_model()

class UserAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = (
            'username', 'nombre', 'apellido', 'tipo_documento', 'numero_documento','tipo_persona', 
            'id','email', 'numeroCelular', 'direccion',)
    list_display_links = (
            'username', 'nombre', 'apellido', 'tipo_documento', 'numero_documento', 'tipo_persona', 
            'id','email', 'numeroCelular', 'direccion',)
    search_fields = (
            'username', 'nombre', 'apellido', 'tipo_documento', 'numero_documento', 'tipo_persona', 
            'id','email', 'numeroCelular', 'direccion',)
    list_per_page = 25
    list_filter = ('nombre',)
    
    
admin.site.register(User, UserAdmin)
admin.site.register(TipoPersona)
admin.site.register(Camiseta)
admin.site.register(CamisetaColor)
#admin.site.register(Catalogo)
admin.site.register(Color)
admin.site.register(DetalleFactura)
#admin.site.register(Estampado)
admin.site.register(Factura)


    
    

