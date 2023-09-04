from django.db import models

# Create your models here.
class Topico(models.Model):
    nome = models.CharField(max_length=264)
    
    def __str__(self):
        return self.nome

class Pagina(models.Model):
    topico = models.ForeignKey(Topico, on_delete=models.CASCADE)
    nome = models.CharField(max_length=264)
    url = models.URLField(unique=True, default=None)
        
    def __str__(self):
        return self.nome

class RegistroAcesso(models.Model):
    pagina = models.ForeignKey(Pagina, on_delete=models.CASCADE)
    data = models.DateField(unique=True)
    
    def __str__(self):
        return str(self.data)

class Produto(models.Model):
    nome = models.CharField(max_length=256)
    valor = models.DecimalField(decimal_places=2, max_digits=9)
    quantidade_estoque = models.IntegerField()
    
    def __str__(self):
        return self.nome
