import allure
import requests

from test_api_kvlad.endpoints.endpoint import Endpoint


class CreateObject(Endpoint):

    @allure.step("Create new object")
    def create_new_object(self, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(
            url=self.url,
            json=payload,
            headers=headers
        )
        if self.response.status_code == 200:
            self.response_text = self.response.text
            self.body = self.response.json()
            self.object_id = self.body['id']
        self.response_text = self.response.text

    @allure.step("Delete new object")
    def delete_new_object(self, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.delete(
            url=f"{self.url}/{self.object_id}",
            headers=headers
        )

    @allure.step("Check invalid response message")
    def check_invalid_response_message(self):
        expected_message = "Invalid parameters"
        assert expected_message in self.response_text,  \
            (f"Expected message: {expected_message},"
             f" Actual message: {self.response_text}")

