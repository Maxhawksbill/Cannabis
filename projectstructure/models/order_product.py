from django.db import models

class OrderProduct(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='order_product')
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='order_product')
    quantity = models.PositiveIntegerField(default=1)

    @property
    def price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.quantity} of {self.product.name} in Order #{self.order.uuid}"
