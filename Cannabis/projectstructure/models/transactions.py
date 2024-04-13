from django.db import models
from order import Order
import uuid

class Transaction(models.Model):
    PAYMENT_METHOD_CHOICES = (
        ('credit_card', 'Credit Card'),
        ('paypal', 'PayPal'),
        ('cash', 'Cash'),
        # Add more choices as needed
    )

    PAYMENT_STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
        # Add more choices as needed
    )

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    order = models.OneToOneField('Order', on_delete=models.CASCADE, related_name='transaction')
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    status = models.CharField(max_length=50, choices=PAYMENT_STATUS_CHOICES, default='pending')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction for Order #{self.order.uuid} - Method: {self.payment_method} - Status: {self.status}"
