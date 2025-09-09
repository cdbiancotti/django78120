from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import login
from usuarios.forms import Registro, EditarPerfil
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from usuarios.models import DatosExtra


def iniciar_sesion(request):
    
    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.get_user()
            
            login(request, usuario)
            
            DatosExtra.objects.get_or_create(user=usuario)
            
            return redirect('inicio')
            
    else:
        formulario = AuthenticationForm()
        
    return render(request, 'usuarios/iniciar_sesion.html', {'formulario': formulario})

def registro(request):
    
    if request.method == "POST":
        formulario = Registro(request.POST)
        if formulario.is_valid():
            formulario.save()
            
            return redirect("iniciar_sesion")
    else:
        formulario = Registro()
        
    return render(request, 'usuarios/registro.html', {'formulario': formulario})

@login_required
def perfil(request):
    return render(request, 'usuarios/perfil.html')

@login_required
def editar_perfil(request):
    
    datos_extra = request.user.datosextra
    
    if request.method == "POST":
        formulario = EditarPerfil(request.POST, request.FILES, instance=request.user)
        if formulario.is_valid():
            
            avatar_nuevo = formulario.cleaned_data.get('avatar')
            
            if avatar_nuevo:
                datos_extra.avatar = avatar_nuevo
                
            datos_extra.save()
            formulario.save()
            return redirect('perfil') 
    else:
        formulario = EditarPerfil(instance=request.user, initial={'avatar': request.user.datosextra.avatar})
    return render(request, 'usuarios/editar_perfil.html', {'formulario': formulario})

class EditarContrasenia(PasswordChangeView):
    template_name = 'usuarios/editar_contrasenia.html'
    success_url = reverse_lazy('perfil')