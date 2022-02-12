from unittest import TestCase
from fastapi.testclient import TestClient

from ..main import app as web_app


class APITestCase(TestCase):
    def setUp(self):
        self.client = TestClient(web_app)

    def test_main_url(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_create_employee(self):
        employee_data = {
            "employee": {
                "first_name": "Иванов",
                "last_name": "Иван",
                "patronymic": "Иванович",
                "position": "manager",
                "date_of_birth": "1980-02-12",
                "phone_number": "+322223322",
            }
        }
        response = self.client.post("/", json=employee_data)
        self.assertEqual(response.status_code, 200)
