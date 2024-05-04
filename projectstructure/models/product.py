from django.db import models
from projectstructure.models.category import Category
from PIL import Image
from django.core.cache import cache
from django.core.files.uploadedfile import SimpleUploadedFile
from io import BytesIO
import os
import time
from django.core.files.base import ContentFile


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    thc_content = models.FloatField()
    cbd_content = models.FloatField()
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='products'
    )

    # @property
    # def additional_metadata(self):
    #     cache_key = f"product_supplier_data_{self.id}"
    #
    #     cached_data = cache.get(cache_key)
    #
    #     if cached_data:
    #         return cached_data
    #
    #     time.sleep(1)
    #     supplier_data = {
    #         "storage_type": "fridge",
    #         "allegriens": [],
    #     }
    #
    #     cache.set(f"product_supplier_data_{self.id}", supplier_data, 60 * 60 * 24)
    #     return supplier_data

    @property
    def _get_FIELD_display(self, **kwargs):
        return f'{self.name} - {self.image.name} - {self.price}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image:
            # Open the image file
            image = Image.open(self.image.path)

            # Resize the image to 200x200
            image.thumbnail((200, 200))

            # Create a thumbnail file name
            thumb_name, thumb_extension = os.path.splitext(self.image.name)
            thumb_filename = thumb_name + "_thumb" + ".jpg"

            # Create a BytesIO buffer to hold the thumbnail image
            temp_thumb = BytesIO()

            # Save the resized image to the BytesIO buffer as JPEG
            image.convert("RGB").save(temp_thumb, format='JPEG')
            temp_thumb.seek(0)

            # Save the thumbnail image to the ImageField
            self.image.save(thumb_filename,
                            SimpleUploadedFile(
                                thumb_filename,
                                temp_thumb.read(),
                                content_type=f"image/jpeg",
                            ),
                            save=False)

            # Save the model again to update the thumbnail image
            super().save(*args, **kwargs)


