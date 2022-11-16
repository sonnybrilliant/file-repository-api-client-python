import os

import requests
from dotenv import load_dotenv

from file_repository_api_client import FileApi

load_dotenv()

url: str = os.getenv("API_ENDPOINT")
guid: str = os.getenv("TEST_FILE_GUID")

api = FileApi(url)

resp: dict = api.retrieve_file(guid)

file_name: str = f"{resp['results']['name']}"

try:
    response = requests.get(resp["results"]["presigned_url"], allow_redirects=True)
    response.raise_for_status()
    with open(file_name, mode="w", encoding="utf-8") as f:
        f.write(response.content.decode("utf-8"))
except requests.exceptions.HTTPError as err:
    print(f"Exception occurred whilst attempting download file from api, error: {err}")
