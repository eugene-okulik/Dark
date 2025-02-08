import pytest
import requests

from tools import get_object_by_id, update_object

BASE_URL = "http://167.172.172.115:52353/object"

# Test data
OBJECT_DATA = {
    "name": "test_name",
    "data": {"test": "test_data"}
}
UPD_OBJECT_DATA = {
    "name": "Teat Name",
    "data": {"Test": "Test Data"}
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


# Tests
@pytest.mark.critical
def test_get_all_objects():
    """
    Verify that all objects can be retrieved from the API.
    The test sends a GET request and asserts the response status code.
    """
    response = requests.get(BASE_URL)
    assert response.status_code == 200


@pytest.mark.medium
@pytest.mark.parametrize("object_data", THREE_OBJECT_DATA)
def test_create_object(object_data):
    """
    Verify that an object can be successfully created.

    The test sends a POST request with different data sets and checks
    the response status, object attributes, and ID assignment.

    :param object_data: Dictionary containing the object data (parametrized).
    """
    # Create object
    response = requests.post(BASE_URL, json=object_data)
    response_data = response.json()

    # Assertions
    assert response.status_code == 200
    assert response_data["name"] == object_data["name"]
    assert response_data["data"] == object_data["data"]
    assert "id" in response_data

    # Cleanup
    requests.delete(f"{BASE_URL}/{response_data['id']}")


def test_retrieve_object_by_id(get_id_of_new_object):
    """
    Verify that an object can be retrieved by its ID.

    The test first creates an object, retrieves it by ID, and checks that
    the response data matches the original object.

    :param get_id_of_new_object: Fixture that returns the ID of a newly
    created object.
    """
    # Create new object and get its id
    object_id = get_id_of_new_object

    # Get object by ID
    response, response_data = get_object_by_id(
        url=BASE_URL,
        object_id=object_id
    )

    # Assertions
    assert response.status_code == 200
    assert response_data["id"] == object_id


def test_update_object_with_put_method(get_id_of_new_object):
    """
    Verify that an object can be fully updated using the PUT method.

    The test modifies an existing object with a PUT request and checks
    if the changes are correctly applied in the response.

    :param get_id_of_new_object: Fixture that returns the ID of a newly
    created object.
    """
    # Create new object
    object_id = get_id_of_new_object

    # Modify created object
    new_payload = UPD_OBJECT_DATA
    response, response_data = update_object(
        url=BASE_URL,
        object_id=object_id,
        payload=new_payload,
        method="PUT"
    )

    # Assertions
    assert response.status_code == 200
    assert response_data["id"] == object_id
    assert response_data["name"] == new_payload["name"]
    assert response_data["data"] == new_payload["data"]


def test_update_object_with_patch_method(get_id_of_new_object):
    """
    Verify that an object can be partially updated using the PATCH method.

    The test sends a PATCH request with a modified payload and verifies
    that the response reflects the applied changes.

    :param get_id_of_new_object: Fixture that returns the ID of a newly
    created object.
    """
    # Create new object
    object_id = get_id_of_new_object

    # Modify created object
    new_payload = UPD_OBJECT_DATA
    response, response_data = update_object(
        url=BASE_URL,
        object_id=object_id,
        payload=new_payload,
        method="PATCH"
    )

    # Assertions
    assert response.status_code == 200
    assert response_data["id"] == object_id
    assert response_data["name"] == new_payload["name"]
    assert response_data["data"] == new_payload["data"]


def test_delete_object(get_id_of_new_object):
    """
    Verify that an object can be successfully deleted by its ID.

    The test creates an object, deletes it, and checks if the response
    confirms the deletion.

    :param get_id_of_new_object: Fixture that returns the ID of a newly
    created object.
    """
    # Create new object ant get its ID
    object_id = get_id_of_new_object

    # Delete object
    response = requests.delete(f"{BASE_URL}/{object_id}")

    # Assertions
    assert response.status_code == 200
    assert f"Object with id {object_id} successfully deleted" in response.text
