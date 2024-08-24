from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)
    data_publi = models.DateField()
    lido = models.BooleanField(default=False)
    nota = models.FloatField(null=True, blank=True)
    comentarios = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.titulo


class Usuario(models.Model):
    usuario = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    livro = models.ForeignKey(Livro, on_delete=models.SET_NULL, null=True, blank=True)  
    
    def __str__(self):
        return self.usuario