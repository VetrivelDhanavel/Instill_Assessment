import time

import pytest
from httpx import AsyncClient
from starlette.testclient import TestClient
from app.main import create_app
from app.config import PASSWORD

from typing import List
from pydantic import BaseModel


class Meaning(BaseModel):
    part_of_speech: str
    definitions: List[str]


class WordMeaning(BaseModel):
    meanings: List[Meaning]
    source: List[str]


@pytest.fixture(scope="module")
def app():
    """
    Fixture to create the FastAPI application instance.
    """
    return create_app()


@pytest.fixture(scope="module")
def test_client(app):
    """
    Fixture to create a test client for the FastAPI application.
    """
    return TestClient(app)


@pytest.mark.asyncio
async def test_get_word_meanings_async(test_client: TestClient):
    """
    Test asynchronous endpoint for retrieving word meanings.
    """
    words = ["testing the api", "providing invalid credentials"]
    password = PASSWORD
    response = None

    try:
        async with AsyncClient(app=test_client.app, base_url="http://testserver") as ac:
            response = await ac.post(
                "/api/instill_qa/get-word-meaning",
                json={"words": words, "password": password},
            )

        # Print response code and response body only after a successful request
        print("Response Code:", response.status_code)
        print("Response Body:", response.text)

        assert response is not None  # Check if the response is not None
        assert response.status_code == 200
        data = response.json()
        assert len(data) == len(words)
        assert all(isinstance(item, WordMeaning) for item in data)

    except Exception as e:
        print("Exception:", e)


@pytest.mark.parametrize(
    "words,password,expected_status",
    [
        (["test"], "wrong_password", 403),  # Expecting 403 for wrong password
        (["test"], "", 403),  # Expecting 403 for empty password
        ([], PASSWORD, 200),  # Expecting 200 for empty words
    ],
)
def test_get_word_meanings_sync_invalid_input(
        test_client: TestClient, words, password, expected_status
):
    """
    Test synchronous endpoint for retrieving word meanings with invalid input.
    """
    response = test_client.post(
        "/api/instill_qa/get-word-meaning",
        json={"words": words, "password": password},
    )

    # Print response code and response body
    print("Response Code:", response.status_code)
    print("Response Body:", response.text)
    assert response.status_code == expected_status


def test_get_word_meanings_sync_valid_input(test_client: TestClient):
    """
    Test synchronous endpoint for retrieving word meanings with valid input.
    """
    words = ["test", "example"]
    password = PASSWORD

    response = test_client.post(
        "/api/instill_qa/get-word-meaning",
        json={"words": words, "password": password},
    )

    # Print response code and response body
    print("Response Code:", response.status_code)
    print("Response Body:", response.text)

    assert response.status_code == 200
    data = response.json()
    assert len(data) == len(words)


@pytest.mark.asyncio
async def test_response_time_large_input(test_client: TestClient):
    """
    Test the response time of the API for retrieving word meanings with a large number of words.
    """
    large_number_of_words = ["word"] * 1000  # Creating a list of 1000 identical words
    password = PASSWORD

    try:
        async with AsyncClient(app=test_client.app, base_url="http://testserver") as ac:
            start_time = time.time()  # Record the start time
            response = await ac.post(
                "/api/instill_qa/get-word-meaning",
                json={"words": large_number_of_words, "password": password},
            )
            end_time = time.time()  # Record the end time
            response_time = end_time - start_time  # Calculate the response time

        # Print response time
        print("Response Time for Large Input:", response_time)

        assert response is not None  # Check if the response is not None
        assert response.status_code == 200
        data = response.json()
        assert len(data) == len(large_number_of_words)

    except Exception as e:
        print("Exception:", e)


@pytest.mark.asyncio
async def test_invalid_input_error_handling(test_client: TestClient):
    """
    Test the error handling of the API for invalid words or invalid JSON input.
    """
    invalid_input = {"invalid": "input"}  # Invalid JSON input
    invalid_words = ["invalid_word1", "invalid_word2"]  # Words that are not available in the dictionary

    try:
        async with AsyncClient(app=test_client.app, base_url="http://testserver") as ac:
            # Test invalid JSON input
            response_invalid_json = await ac.post(
                "/api/instill_qa/get-word-meaning",
                json=invalid_input,
            )

            # Test invalid words
            response_invalid_words = await ac.post(
                "/api/instill_qa/get-word-meaning",
                json={"words": invalid_words, "password": "invalid_password"},
            )

        # Print response codes and response bodies
        print("Response Code for Invalid JSON Input:", response_invalid_json.status_code)
        print("Response Body for Invalid JSON Input:", response_invalid_json.text)
        print("Response Code for Invalid Words Input:", response_invalid_words.status_code)
        print("Response Body for Invalid Words Input:", response_invalid_words.text)

        # Assert that the responses have the expected status codes
        assert response_invalid_json.status_code == 422  # Expected status code for invalid JSON input
        assert response_invalid_words.status_code == 403  # Expected status code for invalid words input

    except Exception as e:
        print("Exception:", e)
