from django.core.management.base import BaseCommand
from random import choice, randint
from myapp.models import OrderModel, ClientModel, ProductModel


class Command(BaseCommand):
    help = ""

    def add_arguments(self, parser):
        parser.add_argument('title', type=str, help='title product')

    def handle(self, *args, **options):
        product = ProductModel.objects.get(title=options['title'])
        orders = OrderModel.objects.filter(product=product)
        for order in orders:
            self.stdout.write(f'{order}')
