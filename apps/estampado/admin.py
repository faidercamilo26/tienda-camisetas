from django.contrib import admin

from apps.estampado.models import Estampado

class EstampadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'artista' ,'nombre', 'precio', 'cantidad', 'ventas' )
    list_display_links = ('id', 'nombre', )
    list_filter = ('category', )
    list_editable = ('precio', 'cantidad', 'ventas' )
    search_fields = ('nombre', 'descripcion', )
    list_per_page = 25

admin.site.register(Estampado, EstampadoAdmin)