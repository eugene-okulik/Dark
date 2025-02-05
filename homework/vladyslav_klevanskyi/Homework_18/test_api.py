import requests

BASE_URL = "http://167.172.172.115:52353/object"


# Helping functions
def get_all_objects() -> requests.Response:
    """
    Fetch all objects from the API.
    :return: Response object from the GET request.
    """
    return requests.get(BASE_URL)


def get_object_by_id(object_id: int) -> tuple:
    """
    Fetch a specific object by its ID.
    :param object_id: ID of the object to retrieve.
    :return: A tuple containing the response object and the JSON-parsed
    response data.
    """
    response = requests.get(BASE_URL + f"/{object_id}")
    response_data = response.json()
    return response, response_data


def post_object(payload: dict) -> tuple:
    """
    Create a new object by sending a POST request.
    :param payload: Data to be sent in the request body.
    :return: A tuple containing the response object and the JSON-parsed
    response data.
    """
    response = requests.post(BASE_URL, json=payload)
    response_data = response.json()
    return response, response_data


def update_object(object_id: int, payload: dict, method: str) -> tuple:
    """
    Update an existing object using either PUT or PATCH method.
    :param object_id: ID of the object to update.
    :param payload: Data to be sent in the request body.
    :param method: HTTP method, either "PUT" or "PATCH".
    :return: A tuple containing the response object and the JSON-parsed
    response data.
    """
    response = None
    if method == "PUT":
        response = requests.put(BASE_URL + f"/{object_id}", json=payload)
    elif method == "PATCH":
        response = requests.patch(BASE_URL + f"/{object_id}", json=payload)
    response_data = response.json()
    return response, response_data


def delete_object(object_id: int) -> requests.Response:
    """
    Delete an object by its ID.
    :param object_id: ID of the object to delete.
    :return: Response object from the DELETE request.
    """
    response = requests.delete(BASE_URL + f"/{object_id}")
    return response


def get_new_object_id() -> int:
    """
    Create a new object and return its ID.
    :return: The ID of the newly created object.
    """
    payload = {
        "name": "test_name",
        "data": {"test": "test_data"}
    }
    _, response_data = post_object(payload=payload)
    return response_data["id"]


# TESTS
def test_get_all_objects():
    """Test that fetching all objects returns a 200 status code."""
    assert get_all_objects().status_code == 200


def test_create_object():
    """Test that an object can be successfully created."""
    # Test data
    payload = {
        "name": "test_name",
        "data": {"test": "test_data"}
    }

    # Create object
    response, response_data = post_object(payload=payload)
    assert response.status_code == 200
    assert response_data["name"] == payload["name"]
    assert "id" in response_data
    assert "data" in response_data

    # Cleanup
    delete_object(response_data["id"])


def test_retrieve_object_by_id():
    """Test retrieving an object by its ID."""
    # Create new object ant get its ID
    object_id = get_new_object_id()

    # Get object by ID
    response, response_data = get_object_by_id(object_id)

    # Assertions
    assert response.status_code == 200
    assert response_data["id"] == object_id
    assert "name" in response_data
    assert "data" in response_data

    # Cleanup
    delete_object(object_id)


def test_update_object_with_put_method():
    """Test updating an object using the PUT method."""
    # Test data
    payload = {
        "name": "Test Name",
        "data": {"test": "test_data"}
    }

    # Create new object
    _, new_object_body = post_object(payload=payload)

    # Modify the object
    new_object_body["name"] = "test_name"
    response, response_data = update_object(
        object_id=new_object_body["id"],
        payload=new_object_body,
        method="PUT"
    )

    # Assertions
    assert response.status_code == 200
    assert response_data["name"] == new_object_body["name"]
    assert response_data["id"] == new_object_body["id"]

    # Cleanup
    delete_object(new_object_body["id"])


def test_update_object_with_patch_method():
    """Test updating an object using the PATCH method."""
    # Test data
    payload = {
        "name": "Test Name",
        "data": {"test": "test_data"}
    }

    # Create new object
    _, new_object_body = post_object(payload=payload)

    # Modify the object
    new_object_body["name"] = "test_name"
    new_payload = {"name": "test_name"}
    response, response_data = update_object(
        object_id=new_object_body["id"],
        payload=new_payload,
        method="PATCH"
    )

    # Assertions
    assert response.status_code == 200
    assert response_data["name"] == new_payload["name"]
    assert response_data["id"] == new_object_body["id"]

    # Cleanup
    delete_object(new_object_body["id"])


def test_delete_object():
    """Test that an object can be successfully deleted."""
    # Create new object ant get its ID
    object_id = get_new_object_id()

    # Delete object
    response = delete_object(object_id)

    # Assertions
    assert response.status_code == 200
    assert f"Object with id {object_id} successfully deleted" in response.text
