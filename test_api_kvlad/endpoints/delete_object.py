import allure
import requests

from test_api_kvlad.endpoints.endpoint import Endpoint


class DeleteObject(Endpoint):

    @allure.step("Delete object by ID")
    def delete_object_by_id(self, object_id):
        self.response = requests.delete(f"{self.url}/{object_id}")
        self.response_text = self.response.text

    @allure.step("Check that the response message is correct")
    def check_response_message_is_correct(self, object_id):
        expected_message = f"Object with id {object_id} successfully deleted"
        assert expected_message in self.response_text,  \
            (f"Expected message: {expected_message},"
             f" Actual message: {self.response_text}")
