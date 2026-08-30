import requests
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Autor, Livro
from .serializers import AutorSerializer, LivroSerializer


class AutorViewSet(viewsets.ModelViewSet):
    """CRUD JSON para autores."""

    queryset = Autor.objects.all()
    serializer_class = AutorSerializer


class LivroViewSet(viewsets.ModelViewSet):
    """CRUD JSON para livros."""

    queryset = Livro.objects.select_related('autor')
    serializer_class = LivroSerializer


@api_view(['GET'])
def pesquisa_google_books(request):
    """Pesquisa livros na API externa Google Books pelo parâmetro ?q=."""
    consulta = request.query_params.get('q', '').strip()
    if not consulta:
        return Response({'erro': 'Informe o termo de busca no parâmetro q.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        resposta = requests.get(
            'https://www.googleapis.com/books/v1/volumes',
            params={'q': consulta, 'maxResults': 5},
            timeout=8,
        )
        resposta.raise_for_status()
        dados = resposta.json()
    except requests.Timeout:
        return Response({'erro': 'A API externa demorou para responder.'}, status=status.HTTP_504_GATEWAY_TIMEOUT)
    except requests.RequestException:
        return Response({'erro': 'Não foi possível consultar a API externa.'}, status=status.HTTP_502_BAD_GATEWAY)
    except ValueError:
        return Response({'erro': 'A API externa retornou uma resposta inválida.'}, status=status.HTTP_502_BAD_GATEWAY)

    livros = []
    for item in dados.get('items', []):
        volume = item.get('volumeInfo', {})
        livros.append({
            'id_externo': item.get('id'),
            'titulo': volume.get('title'),
            'autores': volume.get('authors', []),
            'data_publicacao': volume.get('publishedDate'),
        })
    return Response({'fonte': 'Google Books', 'consulta': consulta, 'livros': livros})
