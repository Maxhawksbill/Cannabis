import django_filters
from .models import (Product, Address, Category, Inventory, Order, OrderProduct, Promotion, Review, Transaction,
                    User, UserProfile)

class ProductFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    category_name = django_filters.CharFilter(field_name='category__name', lookup_expr='icontains')

    class Meta:
        model = Product
        fields = {
            'name': ['icontains'],
            'price': ['lt', 'gt'],
            'category': ['exact'],
            'thc_content': ['exact'],
            'cbd_content': ['exact'],
            'created_at': ['gt', 'lt'],
        }

class AddressFilter(django_filters.FilterSet):
    class Meta:
        model = Address
        fields = {
            'street_address': ['icontains'],
            'city': ['icontains'],
            'state': ['icontains'],
            'postal_code': ['exact'],
            'country': ['exact'],
        }

class CategoryFilter(django_filters.FilterSet):
    class Meta:
        model = Category
        fields = {
            'name': ['icontains'],
            'description': ['icontains'],
        }

class InventoryFilter(django_filters.FilterSet):
    class Meta:
        model = Inventory
        fields = {
            'quantity_available': ['gt', 'lt'],
            'last_restocked_timestamp': ['gt', 'lt'],
        }

class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Order
        fields = {
            'user': ['exact'],
            'status': ['exact'],
            'payment_method': ['exact'],
            'created_at': ['gt', 'lt'],
            'updated_at': ['gt', 'lt'],
        }

class OrderProductFilter(django_filters.FilterSet):
    class Meta:
        model = OrderProduct
        fields = {
            'order': ['exact'],
            'product': ['exact'],
            'quantity': ['gt', 'lt'],
        }

class PromotionFilter(django_filters.FilterSet):
    class Meta:
        model = Promotion
        fields = {
            'code': ['exact'],
            'description': ['icontains'],
            'discount_amount': ['gt', 'lt'],
            'start_date': ['gt', 'lt'],
            'end_date': ['gt', 'lt'],
        }

class ReviewFilter(django_filters.FilterSet):
    class Meta:
        model = Review
        fields = {
            'user': ['exact'],
            'product': ['exact'],
            'rating': ['exact'],
            'timestamp': ['gt', 'lt'],
        }

class TransactionFilter(django_filters.FilterSet):
    class Meta:
        model = Transaction
        fields = {
            'order': ['exact'],
            'payment_method': ['exact'],
            'status': ['exact'],
            'timestamp': ['gt', 'lt'],
        }

class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = {
            'username': ['icontains'],
            'email': ['exact', 'icontains'],
            'role': ['exact'],
            'date_joined': ['gt', 'lt'],
        }

class UserProfileFilter(django_filters.FilterSet):
    class Meta:
        model = UserProfile
        fields = {
            'user': ['exact'],
            'role': ['exact'],
            'first_name': ['icontains'],
            'last_name': ['icontains'],
            'position': ['icontains'],
            'start_working_day': ['gt', 'lt'],
        }

