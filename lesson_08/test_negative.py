import requests
from dotenv import load_dotenv


load_dotenv()


def test_create_project(api_headers, base_url):
    project = {}
    headers = api_headers
    resp = requests.post(f"{base_url}/projects",
                         json=project, headers=headers)
    print("\nRESPONSE BODY:", resp.text)


def test_get_project(create_project, base_url):
    id = create_project
    headers = {"Authorization": "",
               "Content-Type": "application/json"}
    resp = requests.get(f"{base_url}/projects/{id}",
                        headers=headers)
    print("\nRESPONSE BODY:", resp.text)


def test_change_project(create_project, base_url):
    change_status = {
        "deleted": True,
        "title": "тест"
    }
    id = create_project
    headers = {"Authorization": "",
               "Content-Type": "application/json"}
    resp = requests.put(f"{base_url}/projects/{id}",
                        json=change_status, headers=headers)
    print("\nRESPONSE BODY:", resp.text)
