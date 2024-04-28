from django.test import TestCase

from projectstructure.models import Product


class IntegrationTestCase(TestCase):
    def test_products_api(self):
        Product.objects.create(
            name='A product',
            price=40,
            description='A description')

        response = self.client.get('/api/products/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['results'][0]['name'], 'A product')
        self.assertEqual(response.json()['results'][0]['price'], 40)
        self.assertEqual(response.json()['results'][0]['description'], 'A description')

    def test_products_thc_content(self):
        Product.objects.create(
            name='A product',
            price=40,
            description='A description',
            thc_content=10)

        response = self.client.get('/api/products/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['results'], [])
