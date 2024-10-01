from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app.views import IndexView, RoteiroView, AvaliacaoView, CidadeView, EstadioView, TimeView, IngressoView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('roteiro/', RoteiroView.as_view(), name='roteiro'),
    path('avaliacao/', AvaliacaoView.as_view(), name='avaliacao'),  
    path('cidade/', CidadeView.as_view(), name='cidade'),
    path('estadio/', EstadioView.as_view(), name='estadio'),
    path('time/', TimeView.as_view(), name='time'),
    path('ingresso/', IngressoView.as_view(), name='ingresso'),
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
