import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Pilataxi' in response.data

def test_chat(client):
    response = client.post('/chat', json={'msg': 'hola'})
    assert response.status_code == 200
    data = response.get_json()
    assert 'response' in data