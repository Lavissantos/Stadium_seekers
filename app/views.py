from django.shortcuts import redirect, render
from django.views import View
from app.models import Avaliacao, Cidade, Estadio, Preferencias, Roteiro, Ingresso, Time


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


def get(self, request):
        cidades = Cidade.objects.all()
        return render(request, 'cidade.html', {'cidades': cidades})

class EstadioView(View):
    def get(self, request):
        estadio =Estadio.objects.all()
        return render(request, 'estadio.html', {'estadio': estadio})
    
class RoteiroView(View):
    def get(self, request):
        cidades = Cidade.objects.all()
        preferencias = Preferencias.objects.all()
        times = Time.objects.all()
        return render(request, 'roteiro.html', {
            'cidades': cidades,
            'preferencias': preferencias,
            'times': times,
            'estadio': None  
        })

    def post(self, request):
        cidade_id = request.POST.get('cidade')
        preferencia_id = request.POST.get('preferencia')
        time_id = request.POST.get('time')
        print(f"cidade_id: {cidade_id}, preferencia_id: {preferencia_id}, time_id: {time_id}")

        if cidade_id and preferencia_id:
            estadio = Estadio.objects.filter(
                cidade_id=cidade_id,
                preferencia_id=preferencia_id
            )
        else:
            estadio = None

        if estadio:
            print(f"{estadio.count()} estadios encontrados.")
        else:
            print("Nenhum estadio encontrado.")

        cidades = Cidade.objects.all()
        preferencias = Preferencias.objects.all()
        times = Time.objects.all()

        return render(request, 'roteiro.html', {
            'cidades': cidades,
            'preferencias': preferencias,
            'times': times,
            'estadio': estadio  
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
        foto = request.FILES.get('foto')
        Avaliacao.objects.create(estadio_id=estadio_id, analise=analise, foto=foto)
        return redirect('avaliacao')


class CidadeView(View):
    def get(self, request):
        cidades = Cidade.objects.all()
        return render(request, 'cidade.html', {'cidades': cidades})
    
class TimeView(View):
    def get(self, request):
        times = Time.objects.all()  
        return render(request, 'time.html', {'times': times})  

    def post(self, request):
        nome = request.POST.get('nome')
        cidade_id = request.POST.get('cidade')
        estadio_id = request.POST.get('estadio')
        brasao = request.FILES.get('brasao')  

   
        Time.objects.create(
            nome=nome,
            cidade_id=cidade_id,
            estadio_id=estadio_id,
            brasao=brasao  
        )
        return redirect('time') 
    
class IngressoView(View):
    def get(self, request):
        ingressos = Ingresso.objects.all()
        estadio = Estadio.objects.all()
        return render(request, 'ingresso.html', {
            'ingressos': ingressos,
            'estadio': estadio,
        })

    def post(self, request):
        estadio_id = request.POST.get('estadio')
        data = request.POST.get('data')
        preco = request.POST.get('preco')
        Ingresso.objects.create(estadio_id=estadio_id, data=data, preco=preco)
        return redirect('ingresso')