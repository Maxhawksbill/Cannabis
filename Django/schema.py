import graphene
import graphene_django
from graphene_django.types import DjangoObjectType
from graphql import GraphQLError
from projectstructure.models import Product, Order, Category, OrderProduct


class CategoryObjectType(graphene_django.DjangoObjectType):
    class Meta:
        model = Category
        fields = ['name', 'description']


class ProductObjectType(graphene_django.DjangoObjectType):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity', 'thc_content', 'cbd_content', 'category']


class PaginatedProductObjectType(graphene.ObjectType):
    nodes = graphene.List(ProductObjectType)
    total_count = graphene.Int()


class OrderObjectType(graphene_django.DjangoObjectType):
    class Meta:
        model = Order
        fields = ['uuid', 'user', 'products', 'created_at', 'updated_at', 'payment_method']

class OrderProductObjectType(graphene_django.DjangoObjectType):
    class Meta:
        model = OrderProduct
        fields = ['order', 'product', 'quantity']

class Query(graphene.ObjectType):
    products = graphene.Field(PaginatedProductObjectType, offset=graphene.Int(), limit=graphene.Int())
    product = graphene.Field(ProductObjectType, id=graphene.ID())
    orders = graphene.List(OrderObjectType, user_id=graphene.Int())

    def resolve_product(self, info, id):
        # If category selected, then select_related('category')
        selections = info.field_nodes[0].selection_set.selections
        category_selected = any(selection.name.value == 'category' for selection in selections)

        query = Product.objects.all()
        if category_selected:
            query = query.select_related('category')
        try:
            return query.get(id=id)
        except Product.DoesNotExist:
            return None

    def resolve_products(self, info, offset=None, limit=None):
        total_count = Product.objects.count()

        product_qs = Product.objects.all()

        if offset is not None:
            product_qs = product_qs[offset:]
        if limit is not None:
            product_qs = product_qs[:limit]

        return {
            "nodes": product_qs,
            "total_count": total_count,
        }

    def resolve_orders(self, info, user_id=None):
        if user_id is None:
            return Order.objects.all()
        return Order.objects.filter(user_id=user_id)


class CreateProductMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        price = graphene.Decimal(required=True)
        description = graphene.String(required=True)
        thc_content = graphene.Float(required=True)
        cbd_content = graphene.Float(required=False)

    product = graphene.Field(ProductObjectType)
    user_errors = graphene.List(graphene.String)
    error = graphene.String()

    def mutate(self, info, name, price, description, thc_content, cbd_content):
        if price < 0:
            return CreateProductMutation(product=None, user_errors=['Price must be greater than 0'])

        try:
            product = Product.objects.create(name=name, price=price, description=description, thc_content=thc_content, cbd_content=cbd_content)
            return CreateProductMutation(product=product)
        except Exception as e:
            print(e)
            return CreateProductMutation(product=None, error=str(e))


class UpdateProductMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String(required=True)
        price = graphene.Decimal(required=True)
        description = graphene.String(required=True)
        thc_content = graphene.Float(required=True)
        cbd_content = graphene.Float(required=True)

    product = graphene.Field(ProductObjectType)
    user_errors = graphene.List(graphene.String)
    error = graphene.String()

    def mutate(self, info, name=None, price=None, description=None, thc_content=None, cbd_content=None):
        try:
            product = Product.objects.get(id=id)

            if name is not None:
                product.name = name
            if price is not None:
                product.price = price
            if description is not None:
                product.description = description
            if thc_content is not None:
                product.thc_content = thc_content
            if cbd_content is not None:
                product.cbd_content = cbd_content

            product.save()
            return UpdateProductMutation(product=product)
        except Product.DoesNotExist:
            return UpdateProductMutation(product=None, user_errors=['Product not found'])
        except Exception as e:
            return UpdateProductMutation(product=None, error=str(e))


class CreateOrderInput(graphene.InputObjectType):
    user_id = graphene.ID(required=True)
    product_ids = graphene.List(graphene.ID, required=True)

class CreateOrderPayload(graphene.ObjectType):
    order = graphene.Field(OrderObjectType)

class CreateOrderMutation(graphene.Mutation):
    class Arguments:
        input_data = CreateOrderInput(required=True)

    Output = CreateOrderPayload

    @staticmethod
    def mutate(root, info, input_data):
        # Validate input data
        if not input_data['product_ids']:
            raise GraphQLError("At least one product is required to create an order.")

        user_id = input_data['user_id']
        product_ids = input_data['product_ids']

        try:
            user = Order.objects.get(pk=user_id)
        except Order.DoesNotExist:
            raise GraphQLError("User with the provided ID does not exist.")

        products = []
        for product_id in product_ids:
            try:
                product = Product.objects.get(pk=product_id)
                products.append(product)
            except Product.DoesNotExist:
                raise GraphQLError(f"Product with ID {product_id} does not exist.")

        # Create the order
        order = Order.objects.create(user=user)

        # Add products to the order
        order_products = []
        for product in products:
            order_product = OrderProduct.objects.create(order=order, product=product, quantity=1)
            order_products.append(order_product)

        return CreateOrderPayload(order=order_products)


class Mutation(graphene.ObjectType):
    create_product = CreateProductMutation.Field()
    update_product = UpdateProductMutation.Field()
    delete_product = graphene.Boolean(id=graphene.ID(required=True))
    create_order = CreateOrderMutation.Field()

    def resolve_delete_product(self, info, id):
        try:
            Product.objects.get(id=id).delete()
            return True
        except Product.DoesNotExist:
            return False


schema = graphene.Schema(query=Query, mutation=Mutation)
