import datetime

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils.lorem_ipsum import paragraphs, words
import logging

from myapp.forms import ProductForm
from myapp.models import ClientModel, ProductModel, OrderModel

LOGGER = logging.getLogger(__name__)


def index(request):
    LOGGER.info('Index page!')
    return HttpResponse(f'<h1>{words(6)}</h1><br>{paragraphs(6)}')


def about(request):
    LOGGER.info('About page!')
    return HttpResponse(f'<h1>About me!</h1><br>{paragraphs(9)}')


def all_orders_by_client(request, client_id: int):
    client = get_object_or_404(ClientModel, pk=client_id)
    orders = OrderModel.objects.filter(client=client)

    context = {'title': 'Заказы клиента', 'client': client, 'orders': orders}
    return render(request, 'myapp/all_orders_by_client.html', context)


def all_orders_client_sort(request, client_id: int):
    client = get_object_or_404(ClientModel, pk=client_id)
    orders_week = OrderModel.objects.filter(client=client).filter(registration_date__gt=datetime.date.today() -
                                                                                        datetime.timedelta(weeks=1))
    orders_month = OrderModel.objects.filter(client=client).filter(registration_date__gt=datetime.date.today() -
                                                                                         datetime.timedelta(weeks=4))
    orders_year = OrderModel.objects.filter(client=client).filter(registration_date__gt=datetime.date.today() -
                                                                                        datetime.timedelta(weeks=51))

    week = set()
    month = set()
    year = set()
    for order in orders_week:
        for product in order.product.all():
            week.add(product)

    for order in orders_month:
        for product in order.product.all():
            month.add(product)

    for order in orders_year:
        for product in order.product.all():
            year.add(product)
    context = {'week': week, 'month': month, 'year': year, 'client': client}
    return render(request, 'myapp/all_orders_client_sort.html', context)


def product_add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            title = 'Продукт'
            return redirect(f'/product/{product.pk}/', {'title': title})
    else:
        form = ProductForm()
    return render(request, 'myapp/product_add.html', {'form': form})


def product_view(request, product_id: int):
    product = get_object_or_404(ProductModel, pk=product_id)
    return render(request, 'myapp/product.html', {'product': product})
