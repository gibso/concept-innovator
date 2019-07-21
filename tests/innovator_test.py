from flask_api import status

def test_animal_innovation(client):

    response = client.get('/innovator/animal')

    assert response.status_code == status.HTTP_200_OK