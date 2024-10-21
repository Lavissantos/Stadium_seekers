from django.contrib import admin
from .models import *

admin.site.register(Cidade)
admin.site.register(Estadio)
admin.site.register(Avaliacao)
admin.site.register(Time)
admin.site.register(Ingresso)
admin.site.register(Usuario)
admin.site.register(PontoTuristico)
admin.site.register(Roteiro)
admin.site.register(Preferencias)






class TimeAdmin(admin.ModelAdmin):
    list_display = ('nome',)