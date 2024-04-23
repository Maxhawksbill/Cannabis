from rest_framework import viewsets, filters, permissions
from rest_framework.decorators import action
from .models import Product, Address, Category, Inventory, Order, OrderProduct, Promotion, Review, Transaction, User, \
    UserProfile
from .serializers import (ProductSerializer, AddressSerializer, CategorySerializer, InventorySerializer, OrderSerializer,
                         OrderProductSerializer, PromotionSerializer, ReviewSerializer, TransactionSerializer, UserSerializer,
                         UserProfileSerializer)
from .pagination import PagePerPagePagination
from .filters import (AddressFilter, ProductFilter, PromotionFilter, UserFilter, OrderProductFilter, TransactionFilter, UserProfileFilter,
                     CategoryFilter, InventoryFilter, OrderFilter, ReviewFilter)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_class = ProductFilter
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['price', 'created_at']
    pagination_class = PagePerPagePagination

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    filterset_class = AddressFilter
    permission_classes = [permissions.IsAuthenticated]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filterset_class = CategoryFilter
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    filterset_class = InventoryFilter
    permission_classes = [permissions.IsAdminUser]

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filterset_class = OrderFilter
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.request.user.is_superuser:
            queryset = queryset.filter(user=self.request.user)
        return queryset

class OrderProductViewSet(viewsets.ModelViewSet):
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductSerializer
    filterset_class = OrderProductFilter
    permission_classes = [permissions.IsAuthenticated]

class PromotionViewSet(viewsets.ModelViewSet):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer
    filterset_class = PromotionFilter
    permission_classes = [permissions.IsAdminUser]

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filterset_class = ReviewFilter
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    filterset_class = TransactionFilter
    permission_classes = [permissions.IsAdminUser]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filterset_class = UserFilter
    permission_classes = [permissions.IsAdminUser]

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    filterset_class = UserProfileFilter
    permission_classes = [permissions.IsAuthenticated]


