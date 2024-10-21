from django import forms
from .models import *
from .models import Estadio, Avaliacao


class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = '__all__'

class RegistroForm(forms.ModelForm):
    class Meta: 
        model = Usuario
        fields = '__all__'

class LoginForm(forms.ModelForm):
    class Meta: 
        model = Usuario
        fields = ['nome', 'senha']

class EstadioForm(forms.ModelForm):
    class Meta:
        model = Estadio
        fields = ['nome', 'cidade', 'localizacao', 'descricao', 'imagem']

