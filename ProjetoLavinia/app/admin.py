from django.contrib import admin
from .models import Time, Estadio, Usuario, Avaliacao, Ingresso, Quiz  # Importar todos os modelos que você deseja registrar

admin.site.register(Time)
admin.site.register(Estadio)
admin.site.register(Usuario)
admin.site.register(Avaliacao)
admin.site.register(Ingresso)
admin.site.register(Quiz)
