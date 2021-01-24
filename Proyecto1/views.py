from django.http import HttpResponse
import datetime
from django.template import Template, Context

class Persona(object):

    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido


def saludo(request): # Primera vista

    p1=Persona("Carolina","Riquelme")

    #nombre = "Eduardo"
    #apellido = "Serey"

    temasDelCurso=["Plantillas", "Modelos","Formularios","Vistas", "Desplegue"]

    fecha_actual = datetime.datetime.today()
    
    doc_externo=open("Proyecto1\plantillas\miplantilla.html")

    template=Template(doc_externo.read())

    doc_externo.close()

    contexto=Context({"nombre_persona":p1.nombre, 
                    "apellido_persona":p1.apellido,
                    "fechaHora":fecha_actual,
                    "temas":temasDelCurso})

    documento=template.render(contexto)

    return HttpResponse(documento)

def despedida(request): # Primera vista
    return HttpResponse("Hasta luego")

def dameFecha(request):
    fecha_actual = datetime.datetime.today()
    return HttpResponse(fecha_actual)

def calculaEdad(request,edad,agno):
    periodo=agno-2021
    edadFutura=edad+periodo
    text = "En el año ", agno, " tendras ", edadFutura
    return HttpResponse(text)
