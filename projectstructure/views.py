from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

from projectstructure.models.product import Product
from projectstructure.tasks import order_daily_statistics


# Create your views here.
from django.shortcuts import render
from .models import Product

def products_view(request, *args, **kwargs):
    # request.GET {'offset': 1, 'limit': 10}
    offset = request.GET.get('offset', 0)
    limit = request.GET.get('limit', 10)

    products = Product.objects.all()[int(offset):int(offset) + int(limit)]

    return render(request, 'products.html', {'products': products})


def celery_view(request, *args, **kwargs):
    order_daily_statistics.delay()

    return HttpResponse("OK")
