from django.core.management.base import BaseCommand
from myapp.models import ClientModel


class Command(BaseCommand):
    help = "Getting a client from the city."

    def add_arguments(self, parser):
        parser.add_argument('city', type=str, help='City')

    def handle(self, *args, **options):
        city = options['city']
        clients = ClientModel.objects.filter(address__icontains=city)
        self.stdout.write(f'{clients}')

