from django.urls import path
from clientes_app import views

urlpatterns = [
    path('',views.inicio_vista,name="gestionarclientes.html"),
    path("registrarCliente/",views.registrarCliente,name="registrarCliente"),
    path("seleccionarCliente/<codigo>",views.seleccionarCliente,name="seleccionarCliente"),
    path("borrarCliente/<codigo>",views.borrarCliente,name="borrarCliente"),
    path("editarCliente/",views.editarCliente,name="editarCliente")
]
