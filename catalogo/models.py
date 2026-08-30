from django.db import models


class Autor(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    biografia = models.TextField(blank=True)

    class Meta:
        verbose_name = 'autor'
        verbose_name_plural = 'autores'
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Livro(models.Model):
    titulo = models.CharField(max_length=120)
    sinopse = models.TextField(blank=True)
    isbn = models.CharField(max_length=13, blank=True)
    ano_publicacao = models.PositiveIntegerField(null=True, blank=True)
    autor = models.ForeignKey(Autor, on_delete=models.PROTECT, related_name='livros')
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['titulo']

    def __str__(self):
        return self.titulo
