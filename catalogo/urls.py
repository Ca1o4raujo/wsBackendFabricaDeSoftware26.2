from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import AutorViewSet, LivroViewSet, pesquisa_open_library

router = DefaultRouter()
router.register('autores', AutorViewSet, basename='autor')
router.register('livros', LivroViewSet, basename='livro')

urlpatterns = [
    path('', include(router.urls)),
    path('pesquisa-open-library/', pesquisa_open_library, name='pesquisa-open-library'),
]
