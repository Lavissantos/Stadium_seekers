from django.shortcuts import render

from django.views import View

from.models import * 

class IndexView(View):
    def get(self, request):
        return render(request, 'index.html',)
    def post(self, request): 
        pass

class UsuarioView(View):
    def get(self, request, *args, **kwargs):
        usuarios = Usuario.objects.all()
        return render(request, 'usuarios.html', {'usuarios': usuarios})

class EstadioView(View):
    def get(self, request, *args, **kwargs):
        estadios = Estadio.objects.all()
        return render(request, 'estadios.html', {'estadios': estadios})

class TimeView(View):
    def get(self, request, *args, **kwargs):
        times = Time.objects.all()
        return render(request, 'times.html', {'times': times})

class IngressoView(View):
    def get(self, request, *args, **kwargs):
        ingressos = Ingresso.objects.all()
        return render(request, 'ingressos.html', {'ingressos': ingressos})

class QuizView(View):
    def get(self, request, *args, **kwargs):
        quizzes = Quiz.objects.all()
        return render(request, 'quizzes.html', {'quizzes': quizzes})

class AvaliacaoView(View):
    def get(self, request, *args, **kwargs):
        avaliacoes = Avaliacao.objects.all()
        return render(request, 'avaliacoes.html', {'avaliacoes': avaliacoes})
