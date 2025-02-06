import requests
import pytest


# Test data
BASE_URL = "http://167.172.172.115:52353/object"
OBJECT_DATA = {
    "name": "test_name",
    "data": {"test": "test_data"}
}
THREE_OBJECT_DATA = [
    {
        "name": "test_name1",
        "data": {"test": "test_data"}
    },
    {
        "name": "test_name2",
        "data": {"test": "test_data"}
    },
    {
        "name": "test_name3",
        "data": {"test": "test_data"}
    }
]


def create_object(payload: dict) -> tuple:
    """
    Sends a POST request to create a new object.

    :param payload: A dictionary containing the data for the new object.
    :return: A tuple where:
        - The first element is the Response object from the request.
        - The second element is the parsed JSON response as a dictionary.
    """
    response = requests.post(BASE_URL, json=payload)
    response_data = response.json()
    return response, response_data


def get_object_by_id(object_id: int) -> tuple[requests.Response, dict]:
    """
    Fetch a specific object by its ID.

    :param object_id: ID of the object to retrieve.
    :return: A tuple where:
        - The first element is the Response object from the GET request.
        - The second element is the parsed JSON response as a dictionary.
    """
    response = requests.get(f"{BASE_URL}/{object_id}")
    response_data = response.json()
    return response, response_data


def update_object(
        object_id: int,
        payload: dict,
        method: str
) -> tuple[requests.Response, dict]:
    """
    Update an existing object using either the PUT or PATCH method.

    :param object_id: ID of the object to update.
    :param payload: A dictionary containing the updated data.
    :param method: HTTP method to use, either "PUT" or "PATCH".
    :return: A tuple where:
        - The first element is the Response object from the request.
        - The second element is the parsed JSON response as a dictionary.
    :raises ValueError: If an invalid HTTP method is provided.
    """
    if method == "PUT":
        response = requests.put(f"{BASE_URL}/{object_id}", json=payload)
    elif method == "PATCH":
        response = requests.patch(f"{BASE_URL}/{object_id}", json=payload)
    else:
        raise ValueError("Invalid method. Use 'PUT' or 'PATCH'.")

    response_data = response.json()
    return response, response_data


def delete_object(object_id: int) -> requests.Response:
    """
    Delete an object by its ID.

    :param object_id: ID of the object to delete.
    :return: The Response object from the DELETE request.
    """
    response = requests.delete(f"{BASE_URL}/{object_id}")
    return response


@pytest.fixture(scope="session")
def print_log() -> None:
    """
    Print a log message before and after testing.

    This fixture prints "Start testing" before the session begins
    and "Testing completed" after all tests are done.

    :yield: None
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
    - Yields the response and response data.
    - Deletes the created object after the test.

    :yield: A tuple where:
        - The first element is the Response object from the POST request.
        - The second element is the parsed JSON response containing object
         data.
    """
    # New object creation
    response = requests.post(BASE_URL, json=OBJECT_DATA)
    response_data = response.json()

    # Yield ID
    yield response, response_data

    # Cleanup
    delete_object(response_data["id"])
