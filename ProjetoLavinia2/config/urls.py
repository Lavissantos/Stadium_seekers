"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import IndexView, AvaliacaoView, CidadeView, TimeView, IngressoView, EstadioView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('time/', TimeView.as_view(), name='time'),
    path('avaliacao/', AvaliacaoView.as_view(), name='avaliacao'),  
    path('cidade/', CidadeView.as_view(), name='cidade'),
    path('estadio/', EstadioView.as_view(), name='estadio'),
    path('time/', TimeView.as_view(), name='time'),
    path('ingresso/', IngressoView.as_view(), name='ingresso'),

    
]