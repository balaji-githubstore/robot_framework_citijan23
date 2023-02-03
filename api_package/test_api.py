import json

import requests
from assertpy import assert_that


class APIListener:
    BASE_URL = "https://petstore.swagger.io/v2/"

    def read_json(self, file):
        return json.load(open(file))

    def generate_token(self):
        response = requests.get(url=APIListener.BASE_URL + "pet/20051")
        token = response.json()["name"]
        return token


class TestPetShop(APIListener):
    def test_find_by_pet(self):
        response = requests.get(url=APIListener.BASE_URL + "pet/20051")
        assert_that(200).is_equal_to(response.status_code)
        assert_that(20051).is_equal_to(response.json()["id"])

    def test_add_pet(self):
        json_data = self.read_json("../test_data/new_pet.json")
        headers = {
            "Content - Type": "application / json",
            "Cache - Control": "no - cache"
        }
        response = requests.post(url=APIListener.BASE_URL + "pet", headers=headers, json=json_data)
        assert_that(200).is_equal_to(response.status_code)
        assert_that(20051).is_equal_to(response.json()["id"])

    def test_update_pet(self):
        response = requests.get(url=APIListener.BASE_URL + "pet/20051")
        token = response.json()["name"]
        print(token)

        json_data = self.read_json("../test_data/new_pet.json")
        headers = {
            "Content - Type": "application / json",
            "Cache - Control": "no - cache",
            "Authorization": "Bearer " + token
        }
        response = requests.post(url=APIListener.BASE_URL + "pet", headers=headers, json=json_data)
        assert_that(200).is_equal_to(response.status_code)
        assert_that(20051).is_equal_to(response.json()["id"])
