from django.contrib import admin

from models.product import Product
from models.category import Category
from models.order import Order
from models.order_product import OrderProduct
from models.users import User, UserProfile, ExternalUser, InternalUser, AbstractUser
from models.inventory import Inventory
from models.review import Review
from models.address import Address
from models.promotions import Promotion
from models.transactions import Transaction

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderProduct)
admin.site.register(Address)
admin.site.register(Promotion)
admin.site.register(Transaction)
admin.site.register(Review)
admin.site.register(InternalUser)
admin.site.register(AbstractUser)
admin.site.register(ExternalUser)
admin.site.register(InternalUser)
admin.site.register(UserProfile)
admin.site.register(User)
