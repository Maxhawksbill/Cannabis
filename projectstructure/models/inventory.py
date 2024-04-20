from django.db import models
from django.core.exceptions import ValidationError

class Inventory(models.Model):
    product = models.OneToOneField('Product', on_delete=models.CASCADE)
    quantity_available = models.PositiveIntegerField(default=0)
    last_restocked_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Inventory for {self.product.name} - Available: {self.quantity_available}"
