from conftest import client


def test_create_client(auth):
    client_data = {'gender': 'female', 'age': 18.0, 'username': 'john_doe'}
    response = client.post(
        '/api/client/',
        headers={'Authorization': f'Bearer {auth.access_token}'},
        json=client_data
    )

    res_body = response.json()

    assert response.status_code == 200
    assert res_body['gender'] == client_data['gender']
    assert res_body['age'] == client_data['age']
    assert res_body['username'] == client_data['username']


def test_get_clients(auth):
    # clients_data = [
    #     {'gender': 'female', 'age': 18.0, 'region': 'moscow'},
    #     {'gender': 'male', 'age': 56, 'region': 'tokyo'},
    # ]
    # async with async_session() as session:
    #     for data in clients_data:
    #         await ClientDAL.create(session, data=data, user_id=auth.user_id)
    #
    # response = client.get('/api/client/', headers={'Authorization': f'Bearer {auth.access_token}'})
    #
    # assert response.status_code == 200
    pass


def test_delete_client():
    pass
