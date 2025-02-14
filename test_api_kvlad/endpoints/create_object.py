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
