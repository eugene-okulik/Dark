import requests
import pytest

from test_api import BASE_URL, OBJECT_DATA


@pytest.fixture(scope="session")
def print_log() -> None:
    """
    Print a log message before and after testing.

    This fixture prints "Start testing" before the session begins
    and "Testing completed" after all tests are done.
    """
    print("Start testing")
    yield
    print("Testing completed")


@pytest.fixture(scope="function")
def get_all_objects() -> requests.Response:
    """
    Fetch all objects from the API.

    :return: The Response object from the GET request.
    """
    return requests.get(BASE_URL)


@pytest.fixture(scope="function")
def get_id_of_new_object() -> tuple[requests.Response, dict]:
    """
    Create a new object, yield its response data, and clean up after the test.

    This fixture:
    - Creates a new object via a POST request.
    - Yields a tuple containing:
        - The Response object from the POST request.
        - A dictionary with the parsed JSON response containing object data.
    - Deletes the created object after the test.
    """
    # New object creation
    response = requests.post(BASE_URL, json=OBJECT_DATA)
    response_data = response.json()

    # Yield ID
    yield response, response_data

    # Cleanup
    requests.delete(f"{BASE_URL}/{response_data['id']}")
