from django.db import models

class Cidade(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da cidade")
    uf = models.CharField(max_length=2, verbose_name="UF")

    def __str__(self):
        return f"{self.nome}, {self.uf}"

    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"
        ordering = ['nome']


class Preferencias(models.Model):
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade")
    tipo = models.TextField(verbose_name="Tipo de preferência")  

    def __str__(self):
        return f"{self.tipo} em {self.cidade.nome}"

    class Meta:
        verbose_name = "Preferência"
        verbose_name_plural = "Preferências"
        ordering = ['cidade']


class Estadio(models.Model):
    nome = models.CharField(max_length=500, verbose_name="Nome do estádio")  
    descricao = models.TextField(verbose_name="Descrição do estádio")  
    localizacao = models.CharField(max_length=1500, verbose_name="Localização")  
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade")
    preferencia = models.ForeignKey(Preferencias, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Preferência")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Estádio"
        verbose_name_plural = "Estádios"
        ordering = ['nome']


class Avaliacao(models.Model):
    estadio = models.ForeignKey(Estadio, on_delete=models.CASCADE, verbose_name="Estádio")
    analise = models.TextField(verbose_name="Análise")  

    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"
        ordering = ['estadio']


class Ingresso(models.Model):
    estadio = models.ForeignKey(Estadio, on_delete=models.CASCADE, verbose_name="Estádio")
    preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço")
    data = models.DateField(verbose_name="Data do Evento")

    def __str__(self):
        return f"Ingresso para {self.estadio.nome} - {self.preco} R$"

    class Meta:
        verbose_name = "Ingresso"
        verbose_name_plural = "Ingressos"
        ordering = ['data']


class Time(models.Model):
    nome = models.CharField(max_length=500, verbose_name="Nome do Time")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade")
    estadio = models.ForeignKey(Estadio, on_delete=models.CASCADE, verbose_name="Estádio")
    titulo = models.CharField(max_length=500, verbose_name="Títulos")  

    def __str__(self):
        return f"{self.nome} - {self.cidade.nome} ({self.estadio.nome})"

    class Meta:
        verbose_name = "Time"
        verbose_name_plural = "Times"
        ordering = ['nome']
