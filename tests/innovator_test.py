from flask_api import status


def test_concept_specification(client):
    payload = {'concept-name': 'boat'}

    response = client.post('/specify/concept', json=payload)

    assert response.status_code == status.HTTP_200_OK


def test_input_spaces_specification(client):
    payload = {
        'input-space-names': ['house', 'boat']
    }

    response = client.post('/specify/input-spaces', json=payload)

    assert response.status_code == status.HTTP_200_OK
