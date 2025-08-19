from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    
    return render(request, 'inicio/inicio.html')
    
    # return HttpResponse('<h1>HOLA SOY MI PRIMERA VISTA</h1>')