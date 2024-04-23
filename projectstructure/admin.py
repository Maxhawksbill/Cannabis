from django.contrib import admin

from projectstructure.models import (Product, Category, Order, OrderProduct, Address, Promotion, Transaction, Review, Inventory,
                    User)

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderProduct)
admin.site.register(Address)
admin.site.register(Promotion)
admin.site.register(Transaction)
admin.site.register(Review)
# admin.site.register(InternalUser)
# admin.site.register(AbstractUser)
# admin.site.register(ExternalUser)
# admin.site.register(InternalUser)
# admin.site.register(UserProfile)
admin.site.register(User)
