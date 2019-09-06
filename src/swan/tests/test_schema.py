import json

from graphene_django.utils.testing import GraphQLTestCase
from swan.schema import schema
from swan.codec.base62 import base62
from swan.url.models import URL



class SchemaTestCase(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema

    def setUp(self):
        self.url_1 = URL.objects.create(url="https://apple.ca")
        self.url_2 = URL.objects.create(url="https://www.google.com")

    def test_query(self):
        query = '''
        query {
          getUrl: url(url: "https://apple.ca") {
            url
            hashId
          }
        }
        '''
        
        expected = {
          "getUrl": {
            "url": "https://apple.ca",
            "hashId": self.url_1.hash
          }
        }

        response = schema.execute(query)

        self.assertIsNone(response.errors)
        self.assertEqual(response.data, expected)

    def test_all_query(self):
        query = '''
        query {
          allUrls {
            id
            url
            hashId
          }
        }
        '''

        expected = {
            "allUrls": [{"id": str(x.id), "url": x.url, "hashId": x.hash} for x in URL.objects.all()]
        }

        response = schema.execute(query)

        self.assertIsNone(response.errors)
        self.assertEqual(response.data, expected)

    def test_mutation(self):
        url_name = "https://www.theverge.com"
        mutation = '''
        mutation {
          createUrl(url: "%s") {
            ok
            url {
              id
              url
              hashId
            }
          }
        }
        ''' % (url_name)

        response = schema.execute(mutation)

        url = URL.objects.get(url=url_name)

        expected = { "createUrl": {
            "ok": True,
            "url": {
              "id": str(url.id),
              "url": url.url,
              "hashId": url.hash
            }
          }
        }

        self.assertIsNone(response.errors)
        self.assertEqual(response.data, expected)

    def test_mutation_no_duplicates(self):
        mutation = '''
        mutation {
          createUrl(url: "%s") {
            ok
            url {
              id
              url
            }
          }
        }
        ''' % (self.url_2.url)

        expected = {
          "createUrl": {
            "ok": True,
            "url": {
              "id": str(self.url_2.id),
              "url": self.url_2.url,
            }
          }
        }

        response = schema.execute(mutation)

        self.assertIsNone(response.errors)
        self.assertEqual(response.data, expected)
