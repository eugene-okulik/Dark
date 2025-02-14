import allure
import requests

BASE_URL = "http://167.172.172.115:52353/object"


class Endpoint:
    url = BASE_URL
    object_id = None
    response = None
    body = None
    response_text = None
    headers = {"Content-type": "application/json"}

    @allure.step("Check response status code")
    def check_that_status_is(self, code):
        assert self.response.status_code == code,  \
            (f"Expected status code: {code}, Actual status code:"
             f" {self.response.status_code}")

    @allure.step("Check that the field is in the response")
    def check_that_the_field_is_in_response(self, field):
        assert field in self.body, \
            f"Expected '{field}' in response body, but it's not there"

    @allure.step("Check that the 'id' is the same as sent")
    def check_response_id_is_correct(self, obj_id):
        assert self.body['id'] == obj_id, \
            f"Expected id: {obj_id}, Actual id: {self.body['id']}"

    @allure.step("Check that the 'name' is the same as sent")
    def check_response_name_is_correct(self, name):
        assert self.body['name'] == name, \
            f"Expected name: {name}, Actual name: {self.body['name']}"

    @allure.step("Check that the 'data' is the same as sent")
    def check_response_data_is_correct(self, data):
        assert self.body['data'] == data, \
            f"Expected data: {data}, Actual data: {self.body['data']}"

    @allure.step("Check error response message")
    def check_error_response_message(self, expected_message):
        assert expected_message in self.response_text, \
            (f"Expected message: {expected_message},"
             f" Actual message: {self.response_text}")

    @allure.step("Delete object by ID")
    def delete_object_by_id(self, object_id):
        self.response = requests.delete(f"{self.url}/{object_id}")
        self.response_text = self.response.text
