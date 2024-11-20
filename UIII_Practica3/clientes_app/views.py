from django.shortcuts import render,redirect
from .models import Cliente
# Create your views here.

def inicio_vista(request):
    losclientes=Cliente.objects.all()
    return render(request,'gestionarClientes.html',{"misclientes":losclientes})

def registrarMascota(request):
    codigo=request.POST["txtcodigo"]
    numero=request.POST["txtnumero"]
    direccion=request.POST["txtdireccion"]
    interes=request.POST["txtinteres"]
    historial=request.POST["txthistorial"]
    email=request.POST["txtemail"]

    guardarcliente=Cliente.objects.create(codigo=codigo,numero=numero,direccion=direccion,interes=interes,historial=historial,email=email) 

    return redirect('/')

def seleccionarCliente(request,codigo):
    cliente=Cliente.objects.get(codigo=codigo)
    return render(request,"editarCliente.html",{"misclientes":cliente})

def editarCliente(request):
    codigo=request.POST["txtcodigo"]
    numero=request.POST["txtnumero"]
    direccion=request.POST["txtdireccion"]
    interes=request.POST["txtinteres"]
    historial=request.POST["txthistorial"]
    email=request.POST["txtemail"]

    cliente=Cliente.objects.get(codigo=codigo)

    cliente.numero=numero
    cliente.direccion=direccion
    cliente.interes=interes
    cliente.historial=historial
    cliente.email=email

    
    cliente.save()

    return redirect('/')

def borrarBliente(request,codigo):
    cliente=Cliente.objects.get(codigo=codigo)
    cliente.delete()

    return redirect("/")