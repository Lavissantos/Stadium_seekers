from django.shortcuts import render, redirect
from django.views import View
from .models import Cidade, Estadio, Preferencias, Time, Avaliacao, Ingresso

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

class TimeView(View):
    def get(self, request):
        cidades = Cidade.objects.all()
        preferencias = Preferencias.objects.all()
        estadios = None  # Renomeado de 'estadio' para 'estadios' para clareza

        return render(request, 'time.html', {
            'cidades': cidades,
            'preferencias': preferencias,
            'estadios': estadios,
        })

    def post(self, request):
        cidade_id = request.POST.get('cidade')
        preferencia_id = request.POST.get('preferencia')

        if cidade_id and preferencia_id:
            estadios = Estadio.objects.filter(
                cidade_id=cidade_id,
                preferencia_id=preferencia_id
            )
        else:
            estadios = None

        cidades = Cidade.objects.all()
        preferencias = Preferencias.objects.all()

        return render(request, 'time.html', {
            'cidades': cidades,
            'preferencias': preferencias,
            'estadios': estadios
        })

class AvaliacaoView(View):
    def get(self, request):
        estadios = Estadio.objects.all()
        avaliacoes = Avaliacao.objects.all()
        return render(request, 'avaliacao.html', {
            'estadios': estadios,
            'avaliacoes': avaliacoes,
        })

    def post(self, request):
        estadio_id = request.POST.get('estadio')
        analise = request.POST.get('analise')
        Avaliacao.objects.create(estadio_id=estadio_id, analise=analise)
        return redirect('avaliacao')

class CidadeView(View):
    def get(self, request):
        cidades = Cidade.objects.all()
        return render(request, 'cidade.html', {'cidades': cidades})

class EstadioView(View):
    def get(self, request):
        estadios = Estadio.objects.all()
        return render(request, 'estadio.html', {'estadios': estadios})

class IngressoView(View):
    def get(self, request):
        ingressos = Ingresso.objects.all()  # Corrigido para 'ingressos' (plural)
        estadios = Estadio.objects.all()  # Para o formulário de criação
        return render(request, 'ingresso.html', {
            'ingressos': ingressos,
            'estadios': estadios,
        })

    def post(self, request):
        estadio_id = request.POST.get('estadio')
        preco = request.POST.get('preco')
        data = request.POST.get('data')
        
        # Verificação opcional para garantir que todos os campos estão preenchidos
        if estadio_id and preco and data:
            Ingresso.objects.create(estadio_id=estadio_id, preco=preco, data=data)
        
        return redirect('ingresso')  # Redireciona para a lista de ingressos
