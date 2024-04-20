from django.db import models

class Promotion(models.Model):
    code = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    applicable_products = models.ManyToManyField('Product', related_name='promotions', blank=True)
    applicable_categories = models.ManyToManyField('Category', related_name='promotions', blank=True)

    def __str__(self):
        return f"Promotion: {self.code} - Description: {self.description}"
