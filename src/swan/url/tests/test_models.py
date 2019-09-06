from django.test import TestCase
from swan.url.models import URL


class URLTestCase(TestCase):
    def setUp(self):
        self.url_1 = URL.objects.create(url="https://apple.ca")
        self.url_2 = URL.objects.create(url="https://twitter.com")

    def test_get_hash_id(self):
        """Test hash_id query"""
        apple_ca = URL.objects.get(url="https://apple.ca")
        twitter_com = URL.objects.get(url="https://twitter.com")
