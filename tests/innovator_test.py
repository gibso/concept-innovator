from flask_api import status
import json


def test_boat_specification(client):
    response = client.get('/specify/boat')

    assert response.status_code == status.HTTP_200_OK


def test_input_spaces_specification(client):
    payload = {
        'input-space-names': ['house', 'boat']
    }

    response = client.post('/specify/input-spaces', json=payload)

    assert response.status_code == status.HTTP_200_OK
