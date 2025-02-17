import allure
import requests

from test_api_kvlad.data_for_testing import OBJECTS_DATA
from test_api_kvlad.endpoints.endpoint import Endpoint


class RetrieveAllObjects(Endpoint):

    @allure.step("Retrieve all objects")
    def retrieve_all_objects(self):
        self.response = requests.get(self.url)
        if self.response.status_code == 200:
            self.body = self.response.json()
            return self.body
        self.response_text = self.response.text

    @allure.step(
        "Check that the received objects are not less than the created ones"
    )
    def check_retrieved_objects_not_less_than_created(self):
        objects_in_response = len(self.body["data"])
        assert objects_in_response >= len(OBJECTS_DATA), \
            (f"Expected at least {len(OBJECTS_DATA)} objects, but"
             f" received {objects_in_response}")
