from django.http import HttpResponse
import datetime
from django.template import Template, Context

def Inicio (request):
    plantillaExterna = open("C:\GitHub\tienda-camisetas\Plantillas\Inicio.html")
    template = Template (plantillaExterna.read())
    plantillaExterna.close()
    contexto = Context()
    documento = template.render(contexto)
    return HttpResponse(documento)

def Login (request):
    plantillaExterna1 = open("C:\GitHub\tienda-camisetas\Plantillas\Login.html")
    template1 = Template (plantillaExterna1.read())
    plantillaExterna1.close()
    contexto1 = Context()
    documento1 = template1.render(contexto1)
    return HttpResponse(documento1)

def Registro (request):
    plantillaExterna2 = open("C:\GitHub\tienda-camisetas\Plantillas\Registro.html")
    template2 = Template (plantillaExterna2.read())
    plantillaExterna2.close()
    contexto2 = Context()
    documento2 = template2.render(contexto2)
    return HttpResponse(documento2)