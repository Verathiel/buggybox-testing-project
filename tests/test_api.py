import unittest
import json
from app.app import app

class ApiTestCase(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_api_valid_data(self):
        response = self.client.post("/api/submit", data=json.dumps({
            "name": "Veronika",
            "email": "veronika@example.com",
            "age": "25"
        }), content_type='application/json')

        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["name"], "Veronika")
        self.assertEqual(data["email"], "veronika@example.com")
        self.assertEqual(data["age"], "25")

    def test_api_missing_name(self):
        response = self.client.post("/api/submit", data=json.dumps({
            "email": "veronika@example.com",
            "age": "25"
        }), content_type='application/json')

        self.assertEqual(response.status_code, 200)  # BUG: mělo by být chybové
        data = response.get_json()
        self.assertEqual(data.get("name", ""), "")

    def test_api_empty_email(self):
        response = self.client.post("/api/submit", data=json.dumps({
            "name": "Vera",
            "email": "",
            "age": "25"
        }), content_type='application/json')

        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["email"], "")

    def test_api_invalid_age(self):
        response = self.client.post("/api/submit", data=json.dumps({
            "name": "Vera",
            "email": "vera@example.com",
            "age": "-10"
        }), content_type='application/json')

        self.assertEqual(response.status_code, 200)  # BUG: záporný věk projde
        data = response.get_json()
        self.assertEqual(data["age"], "-10")

if __name__ == "__main__":
    unittest.main()
