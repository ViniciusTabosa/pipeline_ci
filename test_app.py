import os
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_code(client):
    resposta = client.get('/')
    assert resposta.status_code == 200

def test_home_mensagem(client):
    resposta = client.get('/')
    dados = resposta.get_json()
    assert dados['mensagem'] == "Bem vindo a API Fast Order!"

def test_soma(client):
    resposta = client.get('/api/soma?a=10&b=5')
    dados = resposta.get_json()
    assert resposta.status_code == 200
    assert dados['resultado'] == '15.0'

def test_desconto_desativado(client, monkeypatch):
    import app as app_module
    monkeypatch.setattr(app_module, 'FEATURE_DESCONTO_PROMO', False)

    resposta = client.get('/api/desconto?valor=100&porcentagem=15')
    assert resposta.status_code == 403
    dados = resposta.get_json()
    assert dados['flag_status'] is False

def test_desconto_ativado(client, monkeypatch):
    import app as app_module
    monkeypatch.setattr(app_module, 'FEATURE_DESCONTO_PROMO', True)

    resposta = client.get('/api/desconto?valor=100&porcentagem=15')
    assert resposta.status_code == 200
    dados = resposta.get_json()
    assert dados['valor_final'] == 85.0
