from django.core.management.base import BaseCommand
from django.utils.lorem_ipsum import words
from random import randint, choice
from myapp.models import ClientModel
import pandas as pd


class Command(BaseCommand):
    help = 'Client create'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Count')

    def handle(self, *args, **options):
        url_city = 'https://w.wiki/96yw'
        url_street = 'https://w.wiki/96yv'

        cities = pd.read_html(url_city)[0]
        city_list = []
        for city in cities['Город']:
            city_list.append(city)

        streets = pd.read_html(url_street)[0]
        streets_list = []
        for street in streets['Имя']:
            streets_list.append(street)

        for i in range(options['count']):
            client = ClientModel(name=f'{words(1, common=False)}',
                                 email=f'{words(1, common=False)}@{words(1, common=False)}.com',
                                 phone_number=f'+79{randint(100_000_000, 999_999_999)}',
                                 address=f'г. {choice(city_list)} ул. {choice(streets_list)} {randint(1, 100)}')
            client.save()
