import pytest
from app import app
from random import randrange

@pytest.fixture
def client():
  app.config['TESTING'] = True
  with app.test_client() as client:
    yield client

def test_home_status_code(client):
  resposta = client.get('/')
  assert resposta.status_code == 200

def test_home_mensagem(client):
  resposta = client.get('/')
  dados = resposta.get_json()
  assert dados['mensagem'] == "Bem-vindo a API FastOrder!"

def test_soma(client):
  x = randrange(-100, 100)
  y = randrange(-100, 100)
  resposta = client.get(f'/api/soma?n1={x}&n2={y}')
  dados = resposta.get_json()
  assert dados['soma'] == 3
