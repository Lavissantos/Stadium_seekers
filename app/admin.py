from django.contrib import admin
from .models import *

admin.site.register(Cidade)
admin.site.register(Estadio)
admin.site.register(Preferencias)
admin.site.register(Avaliacao)
admin.site.register(Roteiro)
admin.site.register(Time)
admin.site.register(Ingresso)


class TimeAdmin(admin.ModelAdmin):
    list_display = ('nome',)