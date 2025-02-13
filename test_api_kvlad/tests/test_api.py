import allure
import pytest

from test_api_kvlad.data_for_testing import (
    OBJECT_DATA,
    OBJECTS_DATA,
    UPD_OBJECT_DATA,
    INVALID_DATA_OBJECTS
)


@allure.title("Retrieve all objects")
@pytest.mark.critical
def test_get_all_objects(create_few_objects, retrieve_objects_endpoint):
    retrieve_objects_endpoint.retrieve_all_objects()
    # Assertions
    retrieve_objects_endpoint.check_that_status_is_200()
    retrieve_objects_endpoint.check_retrieved_objects_not_less_than_created()


@allure.title("Create object")
@pytest.mark.medium
@pytest.mark.parametrize("object_data", OBJECTS_DATA)
def test_create_object(create_object_endpoint, object_data):
    create_object_endpoint.create_new_object(payload=object_data)
    # Assertions
    create_object_endpoint.check_that_status_is_200()
    create_object_endpoint.check_response_name_is_correct(object_data["name"])
    create_object_endpoint.check_response_data_is_correct(object_data["data"])
    create_object_endpoint.check_that_id_field_in_response_data()


@allure.title("Create object with invalid parameters")
@pytest.mark.medium
@pytest.mark.parametrize(
    argnames="object_data",
    argvalues=[data[1] for data in INVALID_DATA_OBJECTS],
    ids=[title[0] for title in INVALID_DATA_OBJECTS]
)
def test_create_object_with_invalid_data(create_object_endpoint, object_data):
    create_object_endpoint.create_new_object(payload=object_data)
    # Assertions
    create_object_endpoint.check_that_status_is_400()
    create_object_endpoint.check_invalid_response_message()


@allure.title("Retrieve object by ID")
@pytest.mark.critical
def test_retrieve_object_by_id(retrieve_object_endpoint, get_id_of_new_object):
    retrieve_object_endpoint.retrieve_object_by_id(
        object_id=get_id_of_new_object
    )
    # Assertions
    retrieve_object_endpoint.check_that_status_is_200()
    retrieve_object_endpoint.check_response_id_is_correct(get_id_of_new_object)
    retrieve_object_endpoint.check_that_name_field_in_response_data()
    retrieve_object_endpoint.check_that_data_field_in_response_data()


@allure.title("Update object with PUT method")
@pytest.mark.medium
def test_update_object_with_put_method(
        update_object_endpoint,
        get_id_of_new_object
):
    update_object_endpoint.update_object_with_put_method(
        payload=UPD_OBJECT_DATA,
        object_id=get_id_of_new_object
    )
    # Assertions
    update_object_endpoint.check_that_status_is_200()
    update_object_endpoint.check_response_id_is_correct(get_id_of_new_object)
    update_object_endpoint.check_response_name_is_correct(
        UPD_OBJECT_DATA["name"]
    )
    update_object_endpoint.check_response_data_is_correct(
        UPD_OBJECT_DATA["data"]
    )


@allure.title("Update object with PATCH method")
@pytest.mark.medium
def test_update_object_with_patch_method(
        update_object_endpoint,
        get_id_of_new_object
):
    payload = {"name": "Test Name"}
    update_object_endpoint.update_object_with_patch_method(
        payload=payload,
        object_id=get_id_of_new_object
    )
    # Assertions
    update_object_endpoint.check_that_status_is_200()
    update_object_endpoint.check_response_id_is_correct(get_id_of_new_object)
    update_object_endpoint.check_response_name_is_correct(
        payload["name"]
    )
    update_object_endpoint.check_response_data_is_correct(
        OBJECT_DATA["data"]
    )


@allure.title("Delete object")
@pytest.mark.low
def test_delete_object(delete_object_endpoint, get_id_of_new_object):
    delete_object_endpoint.delete_object_by_id(object_id=get_id_of_new_object)
    # Assertions
    delete_object_endpoint.check_that_status_is_200()
    delete_object_endpoint.check_response_message_is_correct(
        get_id_of_new_object
    )
