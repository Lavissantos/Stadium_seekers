from django.db import models
from django.core.exceptions import ValidationError


class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    data_nascimento = models.DateField()

    class Meta:
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return self.nome


class Estadio(models.Model):
    nome = models.CharField(max_length=100)
    localizacao = models.CharField(max_length=255)
    capacidade = models.IntegerField()
    data_construcao = models.DateField()

    class Meta:
        verbose_name_plural = 'Estádios'

    def __str__(self):
        return self.nome


class Time(models.Model):
    nome = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estadio = models.ForeignKey(Estadio, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Times'

    def __str__(self):
        return self.nome


class Ingresso(models.Model):
    estadio = models.ForeignKey(Estadio, on_delete=models.CASCADE)
    data_jogo = models.DateField()
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    quantidade_disponivel = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Ingressos'

    def __str__(self):
        return f'{self.estadio.nome} - {self.data_jogo}'


class Quiz(models.Model):
    pergunta = models.CharField(max_length=255)
    resposta_correta = models.CharField(max_length=255)
    alternativas = models.TextField(help_text="Insira as alternativas separadas por vírgula")

    class Meta:
        verbose_name_plural = 'Quizzes'

    def __str__(self):
        return self.pergunta


class Avaliacao(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Usuário")
    estadio = models.ForeignKey(Estadio, on_delete=models.CASCADE, verbose_name="Estádio")
    nota = models.IntegerField(verbose_name="Nota")
    comentario = models.TextField(verbose_name="Comentário", null=True, blank=True)
    data = models.DateField(verbose_name="Data da avaliação")

    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"

    def clean(self):
        if not (1 <= self.nota <= 10):
            raise ValidationError('A nota deve estar entre 1 e 10.')

    def __str__(self):
        return f"Avaliação de {self.usuario} para {self.estadio}"
