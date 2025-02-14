import allure
import requests

from test_api_kvlad.endpoints.endpoint import Endpoint


class RetrieveObject(Endpoint):

    @allure.step("Retrieve object by ID")
    def retrieve_object_by_id(self, object_id):
        self.response = requests.get(f"{self.url}/{object_id}")
        if self.response.status_code == 200:
            self.body = self.response.json()
            return self.body
        self.response_text = self.response.text

    @allure.step("Check invalid message response")
    def check_invalid_message_response(self):
        expected_message = ("The requested URL was not found on the server."
                            " If you entered the URL manually please check "
                            "your spelling and try again.")
        assert expected_message in self.response_text, \
            (f"Expected message: {expected_message},"
             f" Actual message: {self.response_text}")
