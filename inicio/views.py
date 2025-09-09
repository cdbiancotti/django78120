from django.shortcuts import render, redirect
from django.http import HttpResponse
from inicio.models import Auto
from inicio.forms import FormularioCreacionAuto
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def inicio(request):
    
    return render(request, 'inicio/inicio.html')
    
    # return HttpResponse('<h1>HOLA SOY MI PRIMERA VISTA</h1>')
    
# def crear_auto_v1(request, marca, modelo):
    
#     auto = Auto(marca=marca, modelo=modelo)
#     auto.save()
    
#     return render(request, 'inicio/crear_auto_v1.html')

@login_required
def crear_auto_v2(request):
    
    # print(request.GET)
    # print(request.POST)
    
    if request.method == "POST":
        formulario = FormularioCreacionAuto(request.POST, request.FILES)
        if formulario.is_valid():
            marca_nueva = formulario.cleaned_data.get('marca')
            modelo_nueva = formulario.cleaned_data.get('modelo')
            imagen_nueva = formulario.cleaned_data.get('imagen')
            
            auto = Auto(marca=marca_nueva, modelo=modelo_nueva, imagen=imagen_nueva)
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

class ActualizarAuto(LoginRequiredMixin, UpdateView):
    model = Auto
    template_name = "inicio/actualizar_auto.html"
    # fields = ['marca', 'modelo']
    fields = "__all__"
    success_url = reverse_lazy('listado_autos')
    
class EliminarAuto(LoginRequiredMixin, DeleteView):
    model = Auto
    template_name = "inicio/eliminar_auto.html"
    success_url = reverse_lazy('listado_autos')

