from django.core.management.base import BaseCommand
from random import randint
from myapp.models import ProductModel


class Command(BaseCommand):
    help = 'Update product quantity'

    def handle(self, *args, **options):
        products = ProductModel.objects.all()
        for product in products:
            product.quantity *= randint(10, 20)
            product.save()


