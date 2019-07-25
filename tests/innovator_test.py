from flask_api import status

def test_animal_innovation(client):

    response = client.get('/innovator/furniture')

    assert response.status_code == status.HTTP_204_NO_CONTENT