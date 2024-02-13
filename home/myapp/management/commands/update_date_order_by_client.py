import datetime

from django.core.management.base import BaseCommand
from myapp.models import OrderModel, ClientModel


class Command(BaseCommand):
    help = 'Update date'

    def handle(self, *args, **options):
        # client = ClientModel.objects.get(pk=1092)
        # self.stdout.write(f'{client}')
        orders = OrderModel.objects.get(pk=293)
        self.stdout.write(f'{orders}')
        orders.registration_date = datetime.date(2024, 2, 1)
        orders.save()
