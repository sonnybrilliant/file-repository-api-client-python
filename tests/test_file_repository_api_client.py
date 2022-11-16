import responses

from file_repository_api_client import FileApi


@responses.activate
def test_store_file():
    """Test method to store file"""
    responses.add(
        method=responses.POST,
        url="https://file.example.api.com/files",
        json={"results": {"guid": "3843c852-5c98-4a3c-8465-2e92eb2a5711"}},
        status=201,
    )
    api = FileApi("https://file.example.api.com/files")
    response = api.store_file("tests/tests.txt")

    assert response["results"]["guid"] == "3843c852-5c98-4a3c-8465-2e92eb2a5711"
    assert isinstance(response, dict)


@responses.activate
def test_retrieve_file():
    """Test method to retrieve file"""
    responses.add(
        method=responses.GET,
        url="https://file.example.api.com/files/3843c852-5c98-4a3c-8465-2e92eb2a5711",
        json={
            "results": {
                "guid": "3843c852-5c98-4a3c-8465-2e92eb2a5711",
                "presigned_url": "https://file.example.api.com/ff4ddc35-cbfd-48ff-bce2-164b688a714b-tests.txt",
                "name": "tests.txt",
            }
        },
        status=200,
    )
    api = FileApi("https://file.example.api.com/files")
    response = api.retrieve_file(guid="3843c852-5c98-4a3c-8465-2e92eb2a5711")

    assert response["results"]["guid"] == "3843c852-5c98-4a3c-8465-2e92eb2a5711"
    assert (
        response["results"]["presigned_url"]
        == "https://file.example.api.com/ff4ddc35-cbfd-48ff-bce2-164b688a714b-tests.txt"
    )
    assert response["results"]["name"] == "tests.txt"
    assert isinstance(response, dict)
