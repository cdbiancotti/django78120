from django.urls import path
from inicio.views import inicio, crear_auto_v2, listado_autos, detalle_auto, ActualizarAuto, EliminarAuto #, crear_auto_v1

urlpatterns = [
    path('', inicio, name='inicio'),
    # path('crear-auto/<marca>/<modelo>/', crear_auto_v1, name='crear_auto'),
    path('autos/', listado_autos, name='listado_autos'),
    path('autos/crear/', crear_auto_v2, name='crear_auto'),
    path('autos/<auto_id>/', detalle_auto, name='detalle_auto'),
    path('autos/<pk>/actualizar/', ActualizarAuto.as_view(), name='actualizar_auto'),
    path('autos/<pk>/eliminar/', EliminarAuto.as_view(), name='eliminar_auto'),
]
