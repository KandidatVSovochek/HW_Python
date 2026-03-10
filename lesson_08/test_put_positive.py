import requests
import pytest
import os
from dotenv import load_dotenv


load_dotenv()


# создать проект
@pytest.fixture(scope="module")
def create_project():
    project = {"title": "тест"}
    key = os.getenv("YOUGILE_API_KEY")
    headers = {"Authorization": f"Bearer {key}",
               "Content-Type": "application/json"}
    resp = requests.post("https://ru.yougile.com/api-v2/projects",
                         json=project, headers=headers)
    body = resp.json()
    return body["id"]


# изменить проект
def test_change_project(create_project):
    change_status = {
        "deleted": True,
        "title": "тест"
    }
    key = os.getenv("YOUGILE_API_KEY")
    id = create_project
    headers = {"Authorization": f"Bearer {key}",
               "Content-Type": "application/json"}
    resp = requests.put(f"https://ru.yougile.com/api-v2/projects/{id}",
                        json=change_status, headers=headers)
    body = resp.json()
    assert resp.status_code == 200
    print(body)
