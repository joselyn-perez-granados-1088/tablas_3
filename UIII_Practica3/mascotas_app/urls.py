from django.urls import path
from mascotas_app import views

urlpatterns = [
    path('',views.inicio_vista,name="gestionarMascotas.html"),
    path("registrarMascota/",views.registrarMascota,name="registrarMascota"),
    path("seleccionarMascota/<codigo>",views.seleccionarMascota,name="seleccionarMascota"),
    path("borrarMascota/<codigo>",views.borrarMascota,name="borrarMascota"),
    path("editarMascota/",views.editarMascota,name="editarMascota")
]
