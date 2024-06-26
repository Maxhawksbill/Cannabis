from celery import shared_task
from django.core.mail import send_mail, EmailMessage
from rest_framework.authtoken.admin import User

from Google.api import write_to_sheet
from .models import Product, Order, OrderProduct
from telegram.client import send_message
from django.utils import timezone
from datetime import datetime, timedelta
from django.db.models import Sum


@shared_task
def order_send_telegram_message(order_id):
    print('Sending telegram message')
    order = Order.objects.get(uuid=order_id)

    chat_id = 192484569

    order_products = order.order_products.all()
    text = f"New order {order.uuid} created\n"
    for order_product in order_products:
        text += f"{order_product.product.name} - {order_product.quantity} - {order_product.price}\n"

    send_message(chat_id, text)
    print('Telegram message sent')

@shared_task()
def order_daily_statistics():
    print('Sending daily statistics')
    # Count how many orders were created during the last day
    start_of_day = timezone.now() - timedelta(days=1)
    start_date = datetime.combine(start_of_day.date(), datetime.min.time())  # 00:00:00
    end_date = datetime.combine(start_of_day.date(), datetime.max.time())  # 23:59:59

    chat_id = 912697577

    orders = Order.objects.filter(
        created_at__date__range=(start_date, end_date)
    )
    order_count = orders.count()
    order_ids = [order.uuid for order in orders]

    # Identifying Top 3 products
    top_products = OrderProduct.objects.filter(
        order_id__in=order_ids
    ).values('product__name').annotate(total_quantity=Sum('quantity')).order_by('-total_quantity')[:3]

    # Sending message
    text = f"Number of orders created on {start_of_day.date()}: {order_count}\n"
    for idx, product in enumerate(top_products, start=1):
        text += f"{idx}. {product['product__name']} - {product['total_quantity']}\n"

    send_message(chat_id, text)
    print('Daily statistics sent')

@shared_task
def write_google_sheet_products_report():
    products = Product.objects.all()

    # write to google sheet
    products_data = []

    for product in products:
        products_data.append(
            [product.name, float(product.price), product.description])

    # write to google sheet
    write_to_sheet("A:C", products_data)


@shared_task
def send_welcome_email(user_id):
    user = User.objects.get(id=user_id)

    # Send text email
    send_mail(
        'Welcome to our service',
        f'What' / 's up!, {user.username}! Welcome to our service!',
        'm.zabaara@gmail.com',
        ['zabaramax3@gmail.com'],
        fail_silently=False,
    )
