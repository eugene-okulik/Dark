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
    return CreateObject()


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
def id_of_new_object(create_object_endpoint):
    payload = OBJECT_DATA
    create_object_endpoint.create_new_object(payload=payload)
    return create_object_endpoint.object_id


@pytest.fixture(scope="function")
def get_non_existent_id(create_few_objects, retrieve_objects_endpoint):
    all_objects = retrieve_objects_endpoint.retrieve_all_objects()
    return max(int(obj["id"]) for obj in all_objects["data"]) + 11241


@pytest.fixture(scope="function")
def create_few_objects(delete_object_endpoint):
    new_objects = []
    for object_data in OBJECTS_DATA:
        new_object = CreateObject()
        new_object.create_new_object(payload=object_data)
        new_objects.append(new_object)
    yield len(new_objects)
    for new_object in new_objects:
        delete_object_endpoint.delete_object_by_id(new_object.object_id)


@pytest.fixture(autouse=True)
def cleanup(request, create_object_endpoint, delete_object_endpoint):

    def delete_object():
        object_id = create_object_endpoint.object_id
        delete_object_endpoint.delete_object_by_id(object_id)

    request.addfinalizer(delete_object)
