from django.shortcuts import render
from .models import Persona
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return render(request, "inicio.html")

def ingresar(request):
    return render(request, "ingresar.html")

def ingreso(request):
    nombre=request.GET["txt_nombre"]
    appaterno=request.GET["txt_appaterno"]
    apmaterno=request.GET["txt_apmaterno"]
    rut=request.GET["txt_rut"]
    edad=request.GET["txt_edad"]
    vacuna=request.GET["txt_vacuna"]
    fecha=request.GET["txt_fecha"]
    Persona(nombre=nombre,appaterno=appaterno,apmaterno=apmaterno,rut=rut,edad=edad,nomvacuna=vacuna,fecha=fecha).save()
    return HttpResponse("articulo ingresado")

def listar(request):
    
    datos = Persona.objects.all()
    return render(request, "listar.html", {"personas":datos})

def eliminar(request):
    id_recibido = request.GET["rut"]
    persona = Persona.objects.filter(rut=id_recibido)
    if persona:
            pro=Persona.objects.get(rut=id_recibido)
            pro.delete()
            mensaje = "Persona Eliminada..."
    else:
            mensaje = "el id recibido es " + id_recibido
    return HttpResponse(mensaje)

def buscar(request):
    return render(request, 'buscar.html')

def busqueda(request):
    datos = Persona.objects.all()
    query = request.GET["txt_busqueda"]
    busqueda = datos.filter(rut=query)
    if busqueda:
        persona = datos.get(rut=query)
        return render(request, "busqueda.html",  {"persona":persona} )
    else:
        return render(request, "busqueda.html" )