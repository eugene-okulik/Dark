import allure
import requests

from test_api_kvlad.endpoints.endpoint import Endpoint


class UpdateObject(Endpoint):

    @allure.step("Update an object with PUT method")
    def update_object_with_put_method(self, object_id, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(
            url=f"{self.url}/{object_id}",
            json=payload,
            headers=headers
        )
        self.body = self.response.json()

    @allure.step("Update an object with PATCH method")
    def update_object_with_patch_method(self, object_id, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.patch(
            url=f"{self.url}/{object_id}",
            json=payload,
            headers=headers
        )
        self.body = self.response.json()
