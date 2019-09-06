from django.test import TestCase
from django.urls import reverse

from swan.codec.base62 import base62
from swan.url.models import URL


class URLViewTests(TestCase):
    def setUp(self):
        self.url_1 = URL.objects.create(url="https://apple.ca")
        self.url_2 = URL.objects.create(url="https://twitter.com")

    def test_302(self):
        """
        URLView returns a response with status code 302 and
        Location header set correctly.
        """
        url = reverse('hashid', args=(self.url_1.hash,))
        response = self.client.get(url)

        # print('id=%d, hash=%s' % (self.url_1.id, self.url_1.hash))

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'], self.url_1.url)

    def test_404(self):
        """
        URLView returns a response with status code 404 and
        reason 'Short URL not found.' if hashid does not exist.
        """
        hashid = base62.encode(URL.objects.last().id + 1)

        # print('id=%d, hash=%s' % (URL.objects.last().id + 1, hashid))
        
        url = reverse('hashid', args=(hashid,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.reason_phrase, 'Short URL not found.')
