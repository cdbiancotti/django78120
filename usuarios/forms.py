from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms


class Registro(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contrasenia", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contrasenia", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {llave: '' for llave in fields}
        
class EditarPerfil(UserChangeForm):
    password = None
    email = forms.EmailField()
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    avatar = forms.ImageField(required=False)
    
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'avatar']
        help_texts = {llave: '' for llave in fields}