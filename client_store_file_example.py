import os

from dotenv import load_dotenv

from file_repository_api_client import FileApi

load_dotenv()

url: str = os.getenv("API_ENDPOINT")
file: str = os.getenv("TEST_FILE_PATH")

api = FileApi(url)

resp: dict = api.store_file(file)

print(resp)
