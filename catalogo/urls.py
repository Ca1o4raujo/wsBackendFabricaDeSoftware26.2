from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import AutorViewSet, LivroViewSet, pesquisa_google_books

router = DefaultRouter()
router.register('autores', AutorViewSet, basename='autor')
router.register('livros', LivroViewSet, basename='livro')

urlpatterns = [
    path('', include(router.urls)),
    path('pesquisa-google-books/', pesquisa_google_books, name='pesquisa-google-books'),
]
