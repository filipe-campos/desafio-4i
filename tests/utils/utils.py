import random
import string
from typing import Dict

from fastapi.testclient import TestClient

from core.config import settings


def random_lower_string() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=32))


def random_email() -> str:
    return f"{random_lower_string()}@{random_lower_string()}.com"

def random_name() -> str:
    return f"{random_lower_string()} {random_lower_string()}"

def random_cpf() -> str:
    return ""


def get_token_headers(client: TestClient) -> Dict[str, str]:
    login_data = {
        "username": settings.FIRST_SUPERUSER,
        "password": settings.FIRST_SUPERUSER_PASSWORD,
    }

    r = client.post(f"{settings.API_V1_STR}/login", data=login_data)

    tokens = r.json()
    a_token = tokens["access_token"]
    headers = {"Authorization": f"Bearer {a_token}"}

    return headers
