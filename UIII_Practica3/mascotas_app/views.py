from django.shortcuts import render,redirect
from .models import Mascota
# Create your views here.

def inicio_vista(request):
    lasmascotas=Mascota.objects.all()
    return render(request,'gestionarMascotas.html',{"mismascotas":lasmascotas})

def registrarMascota(request):
    codigo=request.POST["txtcodigo"]
    especie=request.POST["txtespecie"]
    tamaño=request.POST["txttamaño"]
    precio=request.POST["txtprecio"]
    dieta=request.POST["txtdieta"]
    temperamento=request.POST["txttemperamento"]
    cuidados=request.POST["txtcuidados"]
    edad=request.POST["txtedad"]

    guardarmascota=Mascota.objects.create(codigo=codigo,especie=especie,tamaño=tamaño,precio=precio,dieta=dieta,temperamento=temperamento,cuidados=cuidados,edad=edad) 

    return redirect('/')

def seleccionarMascota(request,codigo):
    mascota=Mascota.objects.get(codigo=codigo)
    return render(request,"editarMascota.html",{"mismascotas":mascota})

def editarMascota(request):
    codigo=request.POST["txtcodigo"]
    especie=request.POST["txtespecie"]
    tamaño=request.POST["txttamaño"]
    precio=request.POST["txtprecio"]
    dieta=request.POST["txtdieta"]
    temperamento=request.POST["txttemperamento"]
    cuidados=request.POST["txtcuidados"]
    edad=request.POST["txtedad"]

    mascota=Mascota.objects.get(codigo=codigo)

    mascota.especie=especie
    mascota.tamaño=tamaño
    mascota.precio=precio
    mascota.dieta=dieta
    mascota.temperamento=temperamento
    mascota.cuidados=cuidados
    mascota.edad=edad
    
    mascota.save()

    return redirect('/')

def borrarMascota(request,codigo):
    mascota=Mascota.objects.get(codigo=codigo)
    mascota.delete()

    return redirect("/")