from django.db import models
import uuid
from django.core.exceptions import ValidationError
from projectstructure.models import Product

class Order(models.Model):
    PAYMENT_METHOD_CHOICES = (
        ('credit_card', 'Credit Card'),
        ('paypal', 'PayPal'),
        ('cash', 'Cash'),
    )
    uuid = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    status = models.CharField(max_length=50, default='created')  # e.g., pending, processing, completed
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    order_products = models.ManyToManyField(Product, through='OrderProduct')

    def check_product_availability(self):
        for item in self.order_products.all():
            inventory = item.product.inventory
            if inventory.quantity_available < item.quantity:
                raise ValidationError(f"Not enough quantity available for product {item.product.name}")

    @property
    def total_price(self):
        total_price = 0
        for order_product in self.order_products.all():
            total_price += order_product.price
        return total_price

    def save(self, *args, **kwargs):
        self.check_product_availability()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order #{self.uuid} - User: {self.user.username}"

   
