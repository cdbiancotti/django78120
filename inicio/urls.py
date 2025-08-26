from django.urls import path
from inicio.views import inicio, crear_auto_v2, listado_autos #, crear_auto_v1

urlpatterns = [
    path('', inicio, name='inicio'),
    # path('crear-auto/<marca>/<modelo>/', crear_auto_v1, name='crear_auto'),
    path('autos/', listado_autos, name='listado_autos'),
    path('autos/crear/', crear_auto_v2, name='crear_auto'),
]
