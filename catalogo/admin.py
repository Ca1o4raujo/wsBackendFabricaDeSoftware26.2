from django.contrib import admin

from .models import Autor, Livro


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'biografia')
    search_fields = ('nome',)


@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'isbn', 'ano_publicacao', 'criado_em')
    list_filter = ('autor',)
    search_fields = ('titulo',)

# Register your models here.
