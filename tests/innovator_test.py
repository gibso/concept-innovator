from flask_api import status

# def test_animal_innovation(client):
#
#     response = client.get('/innovator/animal')
#
#     assert response.status_code == status.HTTP_204_NO_CONTENT


def test_boathouse_innovation(client):
    response = client.get('/innovator/boathouse')

    assert response.status_code == status.HTTP_204_NO_CONTENT