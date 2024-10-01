from django.db import models

class Cidade(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da cidade")
    uf = models.CharField(max_length=2, verbose_name="UF")

    def __str__(self):
        return f"{self.nome}, {self.uf}"

    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"

class Preferencias(models.Model):
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade")
    tipo = models.TextField(verbose_name="Tipo de preferência") 

    def __str__(self):
        return f"{self.tipo} em {self.cidade.nome}"

    class Meta:
        verbose_name = "Preferência"
        verbose_name_plural = "Preferências"

class Estadio(models.Model):  
    nome = models.CharField(max_length=500, verbose_name="Nome do estadio")
    descricao = models.TextField(verbose_name="Descrição do estadio")
    localizacao = models.CharField(max_length=1500, verbose_name="Localização")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade")
    preferencia = models.ForeignKey(Preferencias, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Preferência")  # "Preferencias" não deve ser capitalizado

    def __str__(self):
        return self.nome
    
    
class Meta:
        verbose_name = "Roteiro"
        verbose_name_plural = "Roteiros"
  
class Avaliacao(models.Model):
    estadio = models.ForeignKey('Estadio', on_delete=models.CASCADE, verbose_name="Estádio")
    analise = models.TextField(verbose_name="Análise")
    foto = models.ImageField(upload_to='avaliacoes/', null=True, blank=True, verbose_name="Foto")

    def __str__(self):
        return f"Avaliação do Estádio {self.estadio.nome}"


class Time(models.Model):
    nome = models.CharField(max_length=100)
    cidade = models.ForeignKey('Cidade', on_delete=models.CASCADE)
    estadio = models.ForeignKey('Estadio', on_delete=models.CASCADE, null=True, blank=True)  # Tornando estádio opcional
    brasao = models.ImageField(upload_to='brasoes/', null=True, blank=True, help_text="Carregue o brasão do time")  # Adicionando help_text

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Time"
        verbose_name_plural = "Times"

class Roteiro(models.Model):
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade")
    preferencias = models.ForeignKey(Preferencias, on_delete=models.CASCADE, verbose_name="Preferências")
    time = models.ForeignKey(Time, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Time")

    def __str__(self):
        return f"Roteiro em {self.cidade.nome}"

    class Meta:
        verbose_name = "Roteiro"
        verbose_name_plural = "Roteiros"

class Ingresso(models.Model):
    estadio = models.ForeignKey(Estadio, on_delete=models.CASCADE, verbose_name="Estádio")
    data = models.DateTimeField(verbose_name="Data do evento")
    preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço")

    def __str__(self):
        return f"Ingresso para {self.estadio.nome} em {self.data.strftime('%d/%m/%Y %H:%M')}"

    class Meta:
        verbose_name = "Ingresso"
        verbose_name_plural = "Ingressos"
    

    

