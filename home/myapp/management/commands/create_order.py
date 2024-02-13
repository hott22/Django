from django.core.management.base import BaseCommand
from random import choice, randint
from myapp.models import OrderModel, ClientModel, ProductModel


class Command(BaseCommand):
    help = "Create order."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Count')

    def handle(self, *args, **options):
        for i in range(options['count']):
            clients = ClientModel.objects.all()
            clients_id_list = []
            for client in clients:
                clients_id_list.append(client.id)

            client = ClientModel.objects.get(pk=choice(clients_id_list))
            products = ProductModel.objects.all()
            products_list = list()
            for i in range(randint(1, len(products))):
                products_list.append(choice(products))
            total_amount = 0
            for product in products_list:
                total_amount += product.price * product.quantity

            order = OrderModel(client=client, total_amount=total_amount)
            order.save()
            order.product.set(products_list)
            order.save()
            # self.stdout.write(f'{order.client}')
