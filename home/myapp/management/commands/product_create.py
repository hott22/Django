from django.core.management.base import BaseCommand
from django.utils.lorem_ipsum import words, paragraphs
from random import randint, choice
from myapp.models import ProductModel


class Command(BaseCommand):
    help = 'Product create'

    def handle(self, *args, **options):
        TITLE = ['молоко', 'хлеб', 'кефир', 'кофе', 'чай', 'творог', 'торт', 'кетчуп', 'майонез', 'масло', 'лимон',
                 'яйцо', 'кока-кола', 'сок']
        for title in TITLE:

            product = ProductModel(title=f'{title}', description=f'{paragraphs(1, common=False)}',
                                   price=randint(100, 10000) / 100, quantity=randint(10, 100))
            product.save()
