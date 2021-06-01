from typing import Dict

from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

import crud
from core.config import settings
from schemas.user import UserCreate
from tests.utils.utils import random_lower_string, random_cpf


def test_create_user_new_cpf(client: TestClient, token_headers: dict, db: Session) -> None:
    username = random_cpf()
    password = random_lower_string()
    data = {"cpf": username, "password": password}

    r = client.post(
        f"{settings.API_V1_STR}/users/", headers=token_headers, json=data,
    )

    assert 200 <= r.status_code < 300

    created_user = r.json()
    user = crud.user.get_by_cpf(db, cpf=username)

    assert user
    assert user.cpf == created_user["cpf"]


def test_get_existing_user(client: TestClient, token_headers: dict, db: Session) -> None:
    username = random_cpf()
    password = random_lower_string()
    user_in = UserCreate(cpf=username, password=password)
    user = crud.user.create(db, obj_in=user_in)
    user_id = user.id

    r = client.get(
        f"{settings.API_V1_STR}/users/{user_id}", headers=token_headers,
    )

    assert 200 <= r.status_code < 300

    existing_user = crud.user.get_by_cpf(db, cpf=username)

    assert existing_user


def test_create_user_existing_username(client: TestClient, token_headers: dict, db: Session) -> None:
    username = random_cpf()
    password = random_lower_string()

    user_in = UserCreate(cpf=username, password=password)
    crud.user.create(db, obj_in=user_in)
    data = {"cpf": username, "password": password}

    r = client.post(
        f"{settings.API_V1_STR}/users/", headers=token_headers, json=data,
    )

    created_user = r.json()

    assert r.status_code == 400
    assert "id" not in created_user


def test_retrieve_users(client: TestClient, token_headers: dict, db: Session) -> None:
    username = random_cpf()
    password = random_lower_string()
    user_in = UserCreate(cpf=username, password=password)
    crud.user.create(db, obj_in=user_in)

    username2 = random_cpf()
    password2 = random_lower_string()
    user_in2 = UserCreate(cpf=username2, password=password2)
    crud.user.create(db, obj_in=user_in2)

    r = client.get(f"{settings.API_V1_STR}/users/", headers=token_headers)
    all_users = r.json()

    assert len(all_users) > 1

    for item in all_users:
        assert "cpf" in item