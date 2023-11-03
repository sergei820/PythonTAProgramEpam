import requests


class TestApi:
    url = "https://api.punkapi.com/v2/beers/8"

    def test_get_request(self):
        response = requests.get(self.url)
        expected_statuscode = 200
        expected_name = "Fake Lager"
        expected_abv = 4.7

        # response.json() -> list[dict, dict, ...]
        for some_dict in response.json():
            if some_dict.get("name"):
                actual_name = some_dict.get("name")
            if some_dict.get("abv"):
                actual_abv = some_dict.get("abv")

        assert response.status_code == expected_statuscode
        assert actual_name == expected_name
        assert actual_abv == expected_abv

    def test_delete_request(self):
        response = requests.delete(self.url)
        expected_statuscode = 404
        expected_message = "No endpoint found that matches '/v2/beers/8'"
        assert response.status_code == expected_statuscode
        assert response.json()["message"] == expected_message
