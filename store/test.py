from django.test import TestCase
from rest_framework import status

# Django Rest Framework
from rest_framework.test import APIClient


class StoreTestCase(TestCase):
    def test_create_store(self):

        client = APIClient()

        test_store = {
            "name": "La Tienda 2",
            "address": "Steinfurter str. 2",
            "city": "Berlin",
            "postcode": 49562,
            "geom": "POINT(151.1957362 -33.8670522)",
        }

        response = client.post("/store/", test_store, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
