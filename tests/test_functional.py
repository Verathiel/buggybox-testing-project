import unittest
from app.app import app

class FormTestCase(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_valid_input(self):
        response = self.client.post("/", data={
            "name": "Veronika",
            "email": "veronika@example.com",
            "age": "25"
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn("Data byla odeslána", response.get_data(as_text=True))

    def test_empty_name(self):
        response = self.client.post("/", data={
            "name": "",
            "email": "veronika@example.com",
            "age": "25"
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn("Data byla odeslána", response.get_data(as_text=True))  # BUG: nemělo by projít

    def test_invalid_email(self):
        response = self.client.post("/", data={
            "name": "Vera",
            "email": "veronikabezzavinace.cz",
            "age": "25"
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn("Data byla odeslána", response.get_data(as_text=True))  # BUG: špatný email projde

    def test_negative_age(self):
        response = self.client.post("/", data={
            "name": "Vera",
            "email": "vera@example.com",
            "age": "-5"
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn("Data byla odeslána", response.get_data(as_text=True))  # BUG: záporný věk projde

if __name__ == "__main__":
    unittest.main()
