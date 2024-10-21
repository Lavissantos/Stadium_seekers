from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('avaliacao/', AvaliacaoView.as_view(), name='avaliacao'),  
    path('cidade/', CidadeView.as_view(), name='cidade'),
    path('estadio/', EstadioView.as_view(), name='estadio'),
    path('time/', TimeView.as_view(), name='time'),
    path('ingresso/', IngressoView.as_view(), name='ingresso'),
    path('registro/', RegistroView.as_view(), name='registro'),
    path('login/', LoginView.as_view(), name='login'),
    path('perfil/', PerfilView.as_view(), name='perfil'),
    path('pontoturistico/', PontoTuristicoView.as_view(), name='pontoturistico'),
    path('roteiro/', RoteiroView.as_view(), name='roteiro'),


    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
