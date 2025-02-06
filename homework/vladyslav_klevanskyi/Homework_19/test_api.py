import pytest

from conftest import (
    get_object_by_id,
    create_object,
    update_object,
    delete_object,
    THREE_OBJECT_DATA
)


@pytest.mark.critical
def test_get_all_objects(get_all_objects, print_log):
    """
    Test retrieving all objects from the API.

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

    :param object_data: A dictionary containing object data (parametrized).
    :param print_log: Fixture that prints log messages before and after the
    test.
    """
    print("before test")
    # Create object
    response, response_data = create_object(payload=object_data)

    # Assertions
    assert response.status_code == 200
    assert response_data["name"] == object_data["name"]
    assert "id" in response_data
    assert "data" in response_data

    # Cleanup
    delete_object(response_data["id"])
    print("after test")


def test_retrieve_object_by_id(get_id_of_new_object, print_log):
    """
    Test retrieving an object by its ID.

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
    response, response_data = get_object_by_id(object_id)

    # Assertions
    assert response.status_code == 200
    assert response_data["id"] == object_id
    assert "name" in response_data
    assert "data" in response_data
    print("after test")


def test_update_object_with_put_method(get_id_of_new_object, print_log):
    """
    Test updating an object using the PUT method.

    :param get_id_of_new_object: Fixture that creates a new object and yields
    its response data.
    :param print_log: Fixture that prints log messages before and after
    the test.
    """
    print("before test")
    # Create new object
    _, new_object_body = get_id_of_new_object

    # Modify created object
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
    print("after test")


def test_update_object_with_patch_method(get_id_of_new_object, print_log):
    """
    Test updating an object using the PATCH method.

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
    response = delete_object(object_id)

    # Assertions
    assert response.status_code == 200
    assert f"Object with id {object_id} successfully deleted" in response.text
    print("after test")
