from django.test import TestCase, Client
from django.urls import reverse
class apiTestCase(TestCase):
    def setUp(self) -> None:
        return super().setUp()
    

    def test_login(self):
        c = Client()
        get_response = c.get(reverse("api:login_api"))
        self.assertEqual(get_response.status_code, 405)