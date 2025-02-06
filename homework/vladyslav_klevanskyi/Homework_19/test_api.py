import pytest
import requests

from tools import get_object_by_id, update_object

BASE_URL = "http://167.172.172.115:52353/object"

# Test data
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


# Tests
@pytest.mark.critical
def test_get_all_objects(get_all_objects, print_log):
    """
    Test retrieving all objects from the API.

    This test verifies that the API successfully returns a list of all objects.

    :param get_all_objects: Fixture that fetches all objects.
    :param print_log: Fixture that prints log messages before and after the
    test.
    """
    print("before test")
    assert get_all_objects.status_code == 200
    print("after test")


@pytest.mark.medium
@pytest.mark.parametrize("object_data", THREE_OBJECT_DATA)
def test_create_object(object_data, print_log):
    """
    Test creating an object with different data sets.

    This test sends a POST request to create an object and verifies
    the response status and returned data.

    :param object_data: A dictionary containing object data (parametrized).
    :param print_log: Fixture that prints log messages before and after the
    test.
    """
    print("before test")
    # Create object
    response = requests.post(BASE_URL, json=object_data)
    response_data = response.json()

    # Assertions
    assert response.status_code == 200
    assert response_data["name"] == object_data["name"]
    assert "id" in response_data
    assert "data" in response_data

    # Cleanup
    requests.delete(f"{BASE_URL}/{response_data['id']}")
    print("after test")


def test_retrieve_object_by_id(get_id_of_new_object, print_log):
    """
    Test retrieving an object by its ID.

    This test verifies that an object can be retrieved by its ID and
    checks that the returned data matches the created object.

    :param get_id_of_new_object: Fixture that creates a new object and yields
    its response data.
    :param print_log: Fixture that prints log messages before and after the
    test.
    """
    print("before test")
    # Create new object and get its id
    response, response_data = get_id_of_new_object
    object_id = response_data["id"]

    # Get object by ID
    response, response_data = get_object_by_id(
        url=BASE_URL,
        object_id=object_id
    )

    # Assertions
    assert response.status_code == 200
    assert response_data["id"] == object_id
    assert "name" in response_data
    assert "data" in response_data
    print("after test")


def test_update_object_with_put_method(get_id_of_new_object, print_log):
    """
    Test updating an object using the PUT method.

    This test updates an existing object by sending a PUT request and
    verifies that the changes are correctly applied.

    :param get_id_of_new_object: Fixture that creates a new object and yields
    its response data.
    :param print_log: Fixture that prints log messages before and after the
    test.
    """
    print("before test")
    # Create new object
    _, new_object_body = get_id_of_new_object

    # Modify created object
    new_object_body["name"] = "test_name"
    response, response_data = update_object(
        url=BASE_URL,
        object_id=new_object_body["id"],
        payload=new_object_body,
        method="PUT"
    )

    # Assertions
    assert response.status_code == 200
    assert response_data["name"] == new_object_body["name"]
    assert int(response_data["id"]) == new_object_body["id"]
    print("after test")


def test_update_object_with_patch_method(get_id_of_new_object, print_log):
    """
    Test updating an object using the PATCH method.

    This test partially updates an existing object and verifies the
    response reflects the changes.

    :param get_id_of_new_object: Fixture that creates a new object and yields
    its response data.
    :param print_log: Fixture that prints log messages before and after the
    test.
    """
    print("before test")
    # Create new object
    _, new_object_body = get_id_of_new_object

    # Modify created object
    new_object_body["name"] = "test_name"
    new_payload = {"name": "test_name"}
    response, response_data = update_object(
        url=BASE_URL,
        object_id=new_object_body["id"],
        payload=new_payload,
        method="PATCH"
    )

    # Assertions
    assert response.status_code == 200
    assert response_data["name"] == new_payload["name"]
    assert response_data["id"] == new_object_body["id"]
    print("after test")


def test_delete_object(get_id_of_new_object, print_log):
    """
    Test deleting an object by its ID.

    This test sends a DELETE request to remove an object and verifies
    the success of the operation through the response.

    :param get_id_of_new_object: Fixture that creates a new object and yields
    its response data.
    :param print_log: Fixture that prints log messages before and after the
    test.
    """
    print("before test")
    # Create new object ant get its ID
    _, response_data = get_id_of_new_object
    object_id = response_data["id"]

    # Delete object
    response = requests.delete(f"{BASE_URL}/{object_id}")

    # Assertions
    assert response.status_code == 200
    assert f"Object with id {object_id} successfully deleted" in response.text
    print("after test")
