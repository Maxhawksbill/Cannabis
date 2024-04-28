from unittest.mock import patch

from django.contrib.auth.models import User
from django.test import TestCase

from projectstructure.models import Product, Order


# Create your tests here.
class ProductTestCase(TestCase):
    def test_str(self):
        product = Product.objects.create(
            name='A product', price=100, description='A description')

        self.assertEqual(str(product), 'A product - 100')


@patch('products.signals.order_send_telegram_message')
@patch('products.signals.send_welcome_email')
class OrderProductTestCase(TestCase):
    def test_price(self, send_welcome_email, order_send_telegram_message):
        product = Product.objects.create(
            name='A product', price=100.1, description='A description')
        order = Order.objects.create(user=User.objects.create(username='test'))

        order_product = product.order_products.create(quantity=2, order=order)

        self.assertEqual(order_product.price, 80.2)
        