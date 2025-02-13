import allure

BASE_URL = "http://167.172.172.115:52353/object"


class Endpoint:
    url = BASE_URL
    object_id = None
    response = None
    body = None
    response_text = None
    headers = {"Content-type": "application/json"}

    @allure.step("Check that response is 200")
    def check_that_status_is_200(self):
        assert self.response.status_code == 200,  \
            (f"Expected status code: 200, Actual status code:"
             f" {self.response.status_code}")

    @allure.step("Check that response is 400")
    def check_that_status_is_400(self):
        assert self.response.status_code == 400,  \
            (f"Expected status code: 400, Actual status code:"
             f" {self.response.status_code}")

    @allure.step("Check that the 'id' field is in the response")
    def check_that_id_field_in_response_data(self):
        assert "id" in self.body, \
            f"Expected 'id' field in response body, but it's not there"

    @allure.step("Check that the 'name' is in the response")
    def check_that_name_field_in_response_data(self):
        assert "name" in self.body, \
            f"Expected 'name' in response body, but it's not there"

    @allure.step("Check that the 'data' field is in the response")
    def check_that_data_field_in_response_data(self):
        assert "data" in self.body, \
            f"Expected 'data' in response body, but it's not there"

    @allure.step("Check that the 'id' is the same as sent")
    def check_response_id_is_correct(self, obj_id):
        assert int(self.body['id']) == obj_id, \
            f"Expected id: {obj_id}, Actual id: {self.body['id']}"  # TODO: delete int()

    @allure.step("Check that the 'name' is the same as sent")
    def check_response_name_is_correct(self, name):
        assert self.body['name'] == name, \
            f"Expected name: {name}, Actual name: {self.body['name']}"

    @allure.step("Check that the 'data' is the same as sent")
    def check_response_data_is_correct(self, data):
        assert self.body['data'] == data, \
            f"Expected data: {data}, Actual data: {self.body['data']}"
