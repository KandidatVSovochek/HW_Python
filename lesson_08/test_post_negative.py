import requests
import os
from dotenv import load_dotenv


load_dotenv()


def test_create_project():
    project = {}
    key = os.getenv("YOUGILE_API_KEY")
    headers = {"Authorization": f"Bearer {key}",
               "Content-Type": "application/json"}
    resp = requests.post("https://ru.yougile.com/api-v2/projects",
                         json=project, headers=headers)
    print("\nRESPONSE BODY:", resp.text)
