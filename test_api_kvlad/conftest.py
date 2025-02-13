import pytest

from test_api_kvlad.data_for_testing import OBJECT_DATA, OBJECTS_DATA
from test_api_kvlad.endpoints.create_object import CreateObject
from test_api_kvlad.endpoints.delete_object import DeleteObject
from test_api_kvlad.endpoints.retrieve_all_objects import RetrieveAllObjects
from test_api_kvlad.endpoints.retrieve_object import RetrieveObject
from test_api_kvlad.endpoints.update_object import UpdateObject


@pytest.fixture(scope="function")
def retrieve_objects_endpoint():
    return RetrieveAllObjects()


@pytest.fixture(scope="function")
def create_object_endpoint():
    new_object = CreateObject()
    yield new_object
    new_object.delete_new_object()


@pytest.fixture(scope="function")
def retrieve_object_endpoint():
    return RetrieveObject()


@pytest.fixture(scope="function")
def update_object_endpoint():
    return UpdateObject()


@pytest.fixture(scope="function")
def delete_object_endpoint():
    return DeleteObject()


@pytest.fixture(scope="function")
def get_id_of_new_object(create_object_endpoint):
    payload = OBJECT_DATA
    create_object_endpoint.create_new_object(payload=payload)
    return create_object_endpoint.object_id


@pytest.fixture(scope="session")
def create_few_objects():
    new_objects = []
    for object_data in OBJECTS_DATA:
        new_object = CreateObject()
        new_object.create_new_object(payload=object_data)
        new_objects.append(new_object)
    yield len(new_objects)
    for new_object in new_objects:
        new_object.delete_new_object()
