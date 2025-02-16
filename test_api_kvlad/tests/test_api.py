import allure
import pytest

from test_api_kvlad.data_for_testing import (
    OBJECT_DATA,
    OBJECTS_DATA,
    UPD_OBJECT_DATA,
    INVALID_DATA,
    PATCH_DATA,
    INVALID_PATCH_DATA,
    MESSAGES
)


@allure.feature("Positive")
@allure.title("Retrieve all objects")
@pytest.mark.critical
def test_get_all_objects(create_few_objects, retrieve_objects_endpoint):
    retrieve_objects_endpoint.retrieve_all_objects()
    # Assertions
    retrieve_objects_endpoint.check_that_status_is(200)
    retrieve_objects_endpoint.check_retrieved_objects_not_less_than_created()


@allure.feature("Positive")
@allure.title("Create object")
@pytest.mark.medium
@pytest.mark.parametrize("object_data", OBJECTS_DATA)
def test_create_object(create_object_endpoint, object_data):
    create_object_endpoint.create_new_object(payload=object_data)
    # Assertions
    create_object_endpoint.check_that_status_is(200)
    create_object_endpoint.check_response_name_is_correct(object_data["name"])
    create_object_endpoint.check_response_data_is_correct(object_data["data"])
    create_object_endpoint.check_that_the_field_is_in_response(field="id")


@allure.feature("Negative")
@allure.title("Create object with invalid parameters")
@pytest.mark.medium
@pytest.mark.parametrize(
    argnames="object_data",
    argvalues=[data[1] for data in INVALID_DATA],
    ids=[title[0] for title in INVALID_DATA]
)
def test_create_object_with_invalid_data(create_object_endpoint, object_data):
    create_object_endpoint.create_new_object(payload=object_data)
    # Assertions
    create_object_endpoint.check_that_status_is(400)
    create_object_endpoint.check_error_response_message(
        expected_message=MESSAGES["invalid parameters"]
    )


@allure.feature("Positive")
@allure.title("Retrieve object by ID")
@pytest.mark.critical
def test_retrieve_object_by_id(retrieve_object_endpoint, id_of_new_object):
    retrieve_object_endpoint.retrieve_object_by_id(
        object_id=id_of_new_object
    )
    # Assertions
    retrieve_object_endpoint.check_that_status_is(200)
    retrieve_object_endpoint.check_response_id_is_correct(id_of_new_object)
    retrieve_object_endpoint.check_that_the_field_is_in_response(field="name")
    retrieve_object_endpoint.check_that_the_field_is_in_response(field="data")


@allure.feature("Negative")
@allure.title("Retrieve object by incorrect ID")
@pytest.mark.critical
def test_retrieve_object_by_incorrect_id(
        get_non_existent_id,
        retrieve_object_endpoint,
):
    retrieve_object_endpoint.retrieve_object_by_id(
        object_id=get_non_existent_id
    )
    # Assertions
    retrieve_object_endpoint.check_that_status_is(404)
    retrieve_object_endpoint.check_error_response_message(
        expected_message=MESSAGES["invalid id"]
    )


@allure.feature("Positive")
@allure.title("Update object with PUT method")
@pytest.mark.medium
def test_update_object_with_put_method(
        update_object_endpoint,
        id_of_new_object
):
    update_object_endpoint.update_object_with_put_method(
        payload=UPD_OBJECT_DATA,
        object_id=id_of_new_object
    )
    # Assertions
    update_object_endpoint.check_that_status_is(200)
    update_object_endpoint.check_response_id_is_correct(id_of_new_object)
    update_object_endpoint.check_response_name_is_correct(
        UPD_OBJECT_DATA["name"]
    )
    update_object_endpoint.check_response_data_is_correct(
        UPD_OBJECT_DATA["data"]
    )


@allure.feature("Negative")
@allure.title("Update object with PUT method and invalid parameters")
@pytest.mark.medium
@pytest.mark.parametrize(
    argnames="update_object_data",
    argvalues=[data[1] for data in INVALID_DATA],
    ids=[title[0] for title in INVALID_DATA]
)
def test_update_object_with_put_method_and_invalid_parameters(
        update_object_endpoint,
        id_of_new_object,
        update_object_data
):
    update_object_endpoint.update_object_with_put_method(
        payload=update_object_data,
        object_id=id_of_new_object
    )
    # Assertions
    update_object_endpoint.check_that_status_is(400)
    update_object_endpoint.check_error_response_message(
        expected_message=MESSAGES["invalid parameters"]
    )


@allure.feature("Positive")
@allure.title("Update object with PATCH method")
@pytest.mark.medium
@pytest.mark.parametrize(
    argnames="update_object_data",
    argvalues=[data[1] for data in PATCH_DATA],
    ids=[title[0] for title in PATCH_DATA]
)
def test_update_object_with_patch_method(
        update_object_endpoint,
        id_of_new_object,
        update_object_data
):
    update_object_endpoint.update_object_with_patch_method(
        payload=update_object_data,
        object_id=id_of_new_object
    )
    # Assertions
    update_object_endpoint.check_that_status_is(200)
    update_object_endpoint.check_response_id_is_correct(id_of_new_object)
    # Check fields when 'name' was updated
    if update_object_data.get("name"):
        update_object_endpoint.check_response_name_is_correct(
            update_object_data["name"]
        )
        update_object_endpoint.check_response_data_is_correct(
            OBJECT_DATA["data"]
        )
    # Check fields when 'data' was updated
    if update_object_data.get("data"):
        update_object_endpoint.check_response_data_is_correct(
            update_object_data["data"]
        )
        update_object_endpoint.check_response_name_is_correct(
            OBJECT_DATA["name"]
        )


@allure.feature("Negative")
@allure.title("Update object with PATCH method and invalid parameters")
@pytest.mark.medium
@pytest.mark.parametrize(
    argnames="update_object_data",
    argvalues=[data[1] for data in INVALID_PATCH_DATA],
    ids=[title[0] for title in INVALID_PATCH_DATA]
)
def test_update_object_with_patch_method_and_invalid_parameters(
        update_object_endpoint,
        id_of_new_object,
        update_object_data
):
    update_object_endpoint.update_object_with_patch_method(
        payload=update_object_data,
        object_id=id_of_new_object
    )
    # Assertions
    update_object_endpoint.check_that_status_is(400)
    update_object_endpoint.check_error_response_message(
        expected_message=MESSAGES["invalid parameters"]
    )


@allure.feature("Positive")
@allure.title("Delete object")
@pytest.mark.low
def test_delete_object(delete_object_endpoint, id_of_new_object):
    delete_object_endpoint.delete_object_by_id(object_id=id_of_new_object)
    # Assertions
    delete_object_endpoint.check_that_status_is(200)
    delete_object_endpoint.check_response_message_is_correct(
        id_of_new_object
    )
