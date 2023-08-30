from django.test import TestCase, Client
from django.urls import reverse


class IndexTest(TestCase):
    def setUp(self) -> None:
        self.index_path = reverse("web:index")
        return super().setUp()
    
    def test_get_response(self):
        c = Client()
        response = c.get(self.index_path)
        self.assertEqual(response.status_code, 200)

    def test_fraud_methods(self):
        c = Client()
        responses = [
            c.post(self.index_path).status_code,
            c.patch(self.index_path).status_code,
            c.delete(self.index_path).status_code,
            c.put(self.index_path).status_code,
        ]
        self.assertFalse(200 in responses)