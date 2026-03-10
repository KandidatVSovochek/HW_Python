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


# получить проект по ID
def test_get_project(create_project):
    id = create_project
    headers = {"Authorization": "",
               "Content-Type": "application/json"}
    resp = requests.get(f"https://ru.yougile.com/api-v2/projects/{id}",
                        headers=headers)
    print("\nRESPONSE BODY:", resp.text)
