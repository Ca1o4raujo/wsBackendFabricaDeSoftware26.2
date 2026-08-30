from unittest.mock import Mock, patch

from django.urls import reverse
from rest_framework.test import APITestCase

from .models import Autor, Livro


class BibliotecaApiTests(APITestCase):
    def setUp(self):
        self.autor = Autor.objects.create(nome='Machado de Assis')
        self.livro = Livro.objects.create(titulo='Dom Casmurro', autor=self.autor, ano_publicacao=1899)

    def test_lista_livros_retorna_livro_e_autor(self):
        resposta = self.client.get('/api/livros/')
        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(resposta.data[0]['titulo'], 'Dom Casmurro')
        self.assertEqual(resposta.data[0]['autor_nome'], 'Machado de Assis')

    def test_cria_autor(self):
        resposta = self.client.post('/api/autores/', {'nome': 'Clarice Lispector', 'biografia': ''}, format='json')
        self.assertEqual(resposta.status_code, 201)
        self.assertTrue(Autor.objects.filter(nome='Clarice Lispector').exists())

    def test_pesquisa_sem_termo_retorna_400(self):
        resposta = self.client.get(reverse('pesquisa-open-library'))
        self.assertEqual(resposta.status_code, 400)

    @patch('catalogo.views.requests.get')
    def test_pesquisa_retorna_livros_da_api(self, requisicao):
        resposta_externa = Mock()
        resposta_externa.json.return_value = {
            'docs': [{'key': '/works/OL1W', 'title': 'Dom Casmurro', 'author_name': ['Machado de Assis']}]
        }
        requisicao.return_value = resposta_externa
        resposta = self.client.get(reverse('pesquisa-open-library'), {'q': 'Machado de Assis'})
        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(resposta.data['livros'][0]['titulo'], 'Dom Casmurro')
