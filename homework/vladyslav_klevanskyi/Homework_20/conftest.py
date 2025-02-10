import allure
import requests
import pytest

from test_api import BASE_URL, OBJECT_DATA


@pytest.fixture(scope="session", autouse=True)
def print_start_and_end_testing_session() -> None:
    """
    Print log messages at the start and end of the test session.

    This fixture runs once per test session:
    - Prints "Start testing" before tests begin.
    - Prints "Testing completed" after all tests finish.
    """
    with allure.step("Start testing"):
        print("Start testing")
    yield
    with allure.step("Testing completed"):
        print("Testing completed")


@pytest.fixture(scope="function", autouse=True)
def print_start_and_end_test() -> None:
    """
    Print log messages before and after each test function.

    This fixture runs before and after every test function:
    - Prints "before test" at the start.
    - Prints "after test" at the end.
    """
    with allure.step("Before test"):
        print("Before test")
    yield
    with allure.step("After test"):
        print("After test")


@pytest.fixture(scope="function")
def get_id_of_new_object() -> int:
    """
    Create a new object, yield its ID, and delete it after the test.

    This fixture:
    - Sends a POST request to create a new object.
    - Yields the object's ID.
    - Sends a DELETE request to remove the object after the test.

    :return: The ID of the created object.
    """
    with allure.step("Create new object and yield its ID"):
        response = requests.post(BASE_URL, json=OBJECT_DATA)
        response_data = response.json()
        yield response_data["id"]

    with allure.step("Delete object from DB"):
        requests.delete(f"{BASE_URL}/{response_data['id']}")
