import allure
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
        "data": {"test1": "test_data1"}
    },
    {
        "name": "test_name2",
        "data": {"test2": "test_data2"}
    },
    {
        "name": "test_name3",
        "data": {"test3": "test_data3"}
    }
]


# Tests
@allure.feature("Objects")
@allure.story("Retrieve")
@allure.title("Retrieve all objects")
@pytest.mark.critical
def test_get_all_objects():
    """
    Verify that all objects can be retrieved from the API.
    The test sends a GET request and asserts the response status code.
    """
    with allure.step("Run get request for get all objects"):
        response = requests.get(BASE_URL)
    with allure.step("Check response code is 200"):
        assert response.status_code == 200


@allure.feature("Object")
@allure.story("Create")
@allure.title("Create object")
@pytest.mark.medium
@pytest.mark.parametrize("object_data", THREE_OBJECT_DATA)
def test_create_object(object_data):
    """
    Verify that an object can be successfully created.

    The test sends a POST request with different data sets and checks
    the response status, object attributes, and ID assignment.

    :param object_data: Dictionary containing the object data (parametrized).
    """
    with allure.step("Create new object"):
        response = requests.post(BASE_URL, json=object_data)
        response_data = response.json()

    with allure.step("Check response code is 200"):
        assert response.status_code == 200
    with allure.step("Check 'name' field in response"):
        assert response_data["name"] == object_data["name"]
    with allure.step("Check 'data' field in response"):
        assert response_data["data"] == object_data["data"]
    with allure.step("Check that the 'id' field is in the response"):
        assert "id" in response_data

    with allure.step("Delete new object from DB"):
        requests.delete(f"{BASE_URL}/{response_data['id']}")


@allure.feature("Object")
@allure.story("Retrieve")
@allure.title("Retrieve object by ID")
def test_retrieve_object_by_id(get_id_of_new_object):
    """
    Verify that an object can be retrieved by its ID.

    The test first creates an object, retrieves it by ID, and checks that
    the response data matches the original object.

    :param get_id_of_new_object: Fixture that returns the ID of a newly
    created object.
    """
    with allure.step("Create new object and get its id"):
        object_id = get_id_of_new_object

    with allure.step("Get object by ID from DB"):
        response, response_data = get_object_by_id(
            url=BASE_URL,
            object_id=object_id
        )

    with allure.step("Check response code is 200"):
        assert response.status_code == 200
    with allure.step("Check 'id' field in response"):
        assert response_data["id"] == object_id


@allure.feature("Object")
@allure.story("Update")
@allure.title("Update object with PUT method")
@allure.issue(
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSIGNA03w7rzbd"
    "CamWamfTvoeDg9_ySvAg3XQ&s",
    "BUG-42"
)
def test_update_object_with_put_method(get_id_of_new_object):
    """
    Verify that an object can be fully updated using the PUT method.

    The test modifies an existing object with a PUT request and checks
    if the changes are correctly applied in the response.

    :param get_id_of_new_object: Fixture that returns the ID of a newly
    created object.
    """
    with allure.step("Create new object and get its id"):
        object_id = get_id_of_new_object

    with allure.step("Modify created object"):
        new_payload = UPD_OBJECT_DATA
        response, response_data = update_object(
            url=BASE_URL,
            object_id=object_id,
            payload=new_payload,
            method="PUT"
        )

    with allure.step("Check response code is 200"):
        assert response.status_code == 200
    with allure.step("Check 'id' field in response"):
        assert response_data["id"] == object_id
    with allure.step("Check 'name' field in response"):
        assert response_data["name"] == new_payload["name"]
    with allure.step("Check 'data' field in response"):
        assert response_data["data"] == new_payload["data"]


@allure.feature("Object")
@allure.story("Update")
@allure.title("Update object with PATCH method")
def test_update_object_with_patch_method(get_id_of_new_object):
    """
    Verify that an object can be partially updated using the PATCH method.

    The test sends a PATCH request with a modified payload and verifies
    that the response reflects the applied changes.

    :param get_id_of_new_object: Fixture that returns the ID of a newly
    created object.
    """
    with allure.step("Create new object and get its id"):
        object_id = get_id_of_new_object

    with allure.step("Modify created object"):
        new_payload = UPD_OBJECT_DATA
        response, response_data = update_object(
            url=BASE_URL,
            object_id=object_id,
            payload=new_payload,
            method="PATCH"
        )

    with allure.step("Check response code is 200"):
        assert response.status_code == 200
    with allure.step("Check 'id' field in response"):
        assert response_data["id"] == object_id
    with allure.step("Check 'name' field in response"):
        assert response_data["name"] == new_payload["name"]
    with allure.step("Check 'data' field in response"):
        assert response_data["data"] == new_payload["data"]


@allure.feature("Object")
@allure.story("Delete")
@allure.title("Delete object")
def test_delete_object(get_id_of_new_object):
    """
    Verify that an object can be successfully deleted by its ID.

    The test creates an object, deletes it, and checks if the response
    confirms the deletion.

    :param get_id_of_new_object: Fixture that returns the ID of a newly
    created object.
    """
    with allure.step("Create new object and get its id"):
        object_id = get_id_of_new_object

    with allure.step("Delete object"):
        response = requests.delete(f"{BASE_URL}/{object_id}")

    with allure.step("Check response code is 200"):
        assert response.status_code == 200
    with allure.step("Check response message"):
        assert (
                   f"Object with id {object_id} successfully deleted"
               ) in response.text
