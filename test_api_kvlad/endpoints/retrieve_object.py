import allure
import requests

from test_api_kvlad.endpoints.endpoint import Endpoint


class RetrieveObject(Endpoint):

    @allure.step("Retrieve object by ID")
    def retrieve_object_by_id(self, object_id):
        self.response = requests.get(f"{self.url}/{object_id}")
        self.body = self.response.json()
