import pytest
import requests
import os
from dotenv import load_dotenv

load_dotenv()


# создание проекта
@pytest.fixture(scope="session")
def create_project():
    project = {"title": "тест"}
    key = os.getenv("YOUGILE_API_KEY")
    headers = {"Authorization": f"Bearer {key}",
               "Content-Type": "application/json"}
    resp = requests.post("https://ru.yougile.com/api-v2/projects",
                         json=project, headers=headers)
    body = resp.json()
    return body["id"]


@pytest.fixture(scope="session")
def base_url():
    return "https://ru.yougile.com/api-v2"


@pytest.fixture(scope="session")
def api_headers():
    key = os.getenv("YOUGILE_API_KEY")
    return {
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json"
        }
