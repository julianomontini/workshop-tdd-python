import requests
from sqlalchemy.orm import Session
from uuid import uuid4

BASE_URL = 'http://localhost:5000'

def test_user_should_be_a_required_parameter():
    response = requests.post(BASE_URL + "/users", json={})
    assert response.status_code == 400
    assert response.json()['message'] == 'user is a required parameter'

def test_should_raise_error_if_user_already_exists(e2e_session: Session):
    user = str(uuid4())

    e2e_session.execute(
        'INSERT INTO bank_accounts(name, balance) VALUES '
        '(:name,:balance)',
        {'name': user, 'balance': 0}
    )
    e2e_session.commit()

    payload = {
        'user': user
    }

    response = requests.post(BASE_URL + "/users", json=payload)
    assert response.status_code == 400
    assert response.json()['message'] == 'User already exists'

def test_should_create_user():
    user = str(uuid4())

    payload = {
        'user': user
    }

    response = requests.post(BASE_URL + "/users", json=payload)

    assert response.status_code == 201
    assert response.json()['message'] == 'Success'