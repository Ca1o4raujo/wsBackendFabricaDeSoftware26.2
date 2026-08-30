from django import forms

from .models import Autor, Livro


class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ('nome', 'biografia')


class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ('titulo', 'sinopse', 'isbn', 'ano_publicacao', 'autor')
