from django import forms
from .models import Cidade, Preferencias, Avaliacao

class RoteiroForm(forms.Form):
    cidade = forms.ModelChoiceField(queryset=Cidade.objects.all(), label="Selecione a Cidade")
    preferencia = forms.ModelChoiceField(queryset=Preferencias.objects.all(), label="Selecione a Preferência")

class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = ['estadio', 'analise']
        widgets = {
            'estadio': forms.Select(attrs={'class': 'form-control'}),
            'analise': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
        labels = {
            'estadio': 'Ponto Turístico',
            'analise': 'Análise',
        }