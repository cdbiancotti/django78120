from django.urls import path
from usuarios.views import iniciar_sesion, registro, perfil, editar_perfil, EditarContrasenia
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('iniciar-sesion/', iniciar_sesion, name="iniciar_sesion"),
    path('registro/', registro, name="registro"),
    path('perfil/', perfil, name="perfil"),
    path('perfil/editar/', editar_perfil, name="editar_perfil"),
    path('perfil/editar/contrasenia/', EditarContrasenia.as_view(), name="editar_contrasenia"),
    path('cerrar-sesion/', LogoutView.as_view(template_name="usuarios/cerrar_sesion.html"), name="cerrar_sesion"),
]
