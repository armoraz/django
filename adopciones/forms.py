from django import forms
from .models import Perro, UsuarioAdoptante

class UsuarioAdoptanteForm(forms.ModelForm):
    class Meta:
        model = UsuarioAdoptante
        fields = '__all__'

class PerroForm(forms.ModelForm):
    class Meta:
        model = Perro
        fields = '__all__'

class BuscarPerroForm(forms.Form):
    raza = forms.CharField(max_length=50, required=False)
    edad = forms.IntegerField(required=False)
    tamaño = forms.CharField(max_length=20, required=False)