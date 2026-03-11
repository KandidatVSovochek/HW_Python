import requests
from dotenv import load_dotenv

load_dotenv()


def test_create_project(base_url, api_headers):
    project = {"title": "тест"}
    headers = api_headers
    resp = requests.post(f"{base_url}/projects",
                         json=project, headers=headers)
    print("\nRESPONSE BODY:", resp.text)
    assert resp.status_code == 201


def test_change_project(create_project, base_url, api_headers):
    change_status = {
        "deleted": True,
        "title": "тест"
    }
    id = create_project
    headers = api_headers
    resp = requests.put(f"{base_url}/projects/{id}",
                        json=change_status, headers=headers)
    body = resp.json()
    assert resp.status_code == 200
    print(body)


def test_get_project(create_project, base_url, api_headers):
    id = create_project
    headers = api_headers
    resp = requests.get(f"{base_url}/projects/{id}",
                        headers=headers)
    body = resp.json()
    assert resp.status_code == 200
    print(body)
