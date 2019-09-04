from flask_api import status


def test_boat_specification(client):
    response = client.get('/specify/boat')

    assert response.status_code == status.HTTP_200_OK
