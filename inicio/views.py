from django.shortcuts import render, redirect
from django.http import HttpResponse
from inicio.models import Auto
from inicio.forms import FormularioCreacionAuto
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy

def inicio(request):
    
    return render(request, 'inicio/inicio.html')
    
    # return HttpResponse('<h1>HOLA SOY MI PRIMERA VISTA</h1>')
    
# def crear_auto_v1(request, marca, modelo):
    
#     auto = Auto(marca=marca, modelo=modelo)
#     auto.save()
    
#     return render(request, 'inicio/crear_auto_v1.html')


def crear_auto_v2(request):
    
    # print(request.GET)
    # print(request.POST)
    
    if request.method == "POST":
        formulario = FormularioCreacionAuto(request.POST)
        if formulario.is_valid():
            marca_nueva = formulario.cleaned_data.get('marca')
            modelo_nueva = formulario.cleaned_data.get('modelo')
            
            auto = Auto(marca=marca_nueva, modelo=modelo_nueva)
            auto.save()
            
            return redirect("listado_autos")
            
    else:
        formulario = FormularioCreacionAuto()
    
    return render(request, 'inicio/crear_auto_v2.html', {'formulario': formulario})

def listado_autos(request):
    
    autos = Auto.objects.all()
    
    return render(request, 'inicio/listado_autos.html', {'listado_de_autos': autos})

def detalle_auto(request, auto_id):
    
    auto = Auto.objects.get(id=auto_id)
    
    return render(request, 'inicio/detalle_auto.html', {'auto': auto})

# def actualizar_auto(request, auto_id):
    
#     ...

class ActualizarAuto(UpdateView):
    model = Auto
    template_name = "inicio/actualizar_auto.html"
    # fields = ['marca', 'modelo']
    fields = "__all__"
    success_url = reverse_lazy('listado_autos')
    
class EliminarAuto(DeleteView):
    model = Auto
    template_name = "inicio/eliminar_auto.html"
    success_url = reverse_lazy('listado_autos')

