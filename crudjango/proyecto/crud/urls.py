from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
#     path("agregar/", views.agregar, name="agregar"),
#     path("eliminar/<int:nombre_id>/", views.eliminar, name="eliminar"),
#     path("editar/<int:nombre_id>/", views.editar, name="editar"),
 ]