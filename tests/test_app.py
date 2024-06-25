from http import HTTPStatus

# DONT REPEAT YOUR SELF DRY


def test_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'my json file'}  # Assert


# def test_deve_retornar_ok_e_html():
#     client = TestClient(app)  # Arrange
#     response = client.get('/endpoint')
#     assert response.status_code == 200
#     assert response.text == '<html><body><h1>olá Mundo</h1></body></html>'


def test_create_user(client):
    response = client.post(  # Envio
        '/users/',
        json={
            'username': 'testusername',
            'password': '123',
            'email': 'test@test.com',
        },
    )

    # Validou o status code correto?
    assert response.status_code == HTTPStatus.CREATED

    # Validar o UserPublic
    assert response.json() == {
        'username': 'testusername',
        'id': 1,
        'email': 'test@test.com',
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'testusername',
                'id': 1,
                'email': 'test@test.com',
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'password': '123',
            'username': 'testusername2',
            'id': 1,
            'email': 'test@test.com',
        },
    )

    assert response.json() == {
        'username': 'testusername2',
        'id': 1,
        'email': 'test@test.com',
    }


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.json() == {'message': 'User deleted'}
