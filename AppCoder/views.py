from django.shortcuts import render
from AppCoder.models import Curso, Entregable
from django.http import HttpResponse

# Create your views here.

def curso(request): 
    materia = Curso(nombre="Hacking", camada=99999)

    materia.save()

    return HttpResponse(f"Estoy guardando el primer curso: {materia.nombre}")

def entregables(request):

    ente1 = Entregable(nombre="Examen 1", fechaEntrega = "2022-08-09")

    ente1.save() #guadar en base de datos

    return HttpResponse(f"He guardado: {ente1.nombre} con fecha {ente1.fechaEntrega}")
