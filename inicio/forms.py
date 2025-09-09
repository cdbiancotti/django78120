from django import forms

class FormularioCreacionAuto(forms.Form):
    marca = forms.CharField(max_length=20)
    modelo = forms.CharField(max_length=20)
    imagen = forms.ImageField(required=False)