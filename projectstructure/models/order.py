from django.db import models
import uuid
from django.core.exceptions import ValidationError
from projectstructure.models import Product

class Order(models.Model):
    PAYMENT_METHOD_CHOICES = (
        ('credit_card', 'Credit Card'),
        ('paypal', 'PayPal'),
        ('cash', 'Cash'),
        # Add more choices as needed
    )
    uuid = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)  # e.g., pending, processing, completed
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    order_products = models.ManyToManyField(Product, through='OrderProduct')

    def check_product_availability(self):
        for item in self.order_products.all():
            inventory = item.product.inventory
            if inventory.quantity_available < item.quantity:
                raise ValidationError(f"Not enough quantity available for product {item.product.name}")

    def save(self, *args, **kwargs):
        self.check_product_availability()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order #{self.id} - User: {self.user.username}"
   
