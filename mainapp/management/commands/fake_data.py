from random import randint
from typing import Any
from django.core.management.base import BaseCommand
from mainapp.models import Client, Product, Order


class Command(BaseCommand):
    help = 'Generate fake authors and posts'

    def add_arguments(self, parser) -> None:
        parser.add_argument('count', type=int, help='count')


    def handle(self, *args, **kwargs) -> str | None:
        count = kwargs.get('count')
        # for i in range(1, count+1):
        #     client = Client(name=f'Name{i}', 
        #                     email=f'mail{i}@example.com',
        #                     phone=f'{str(i)}-1111111',
        #                     adress=f'Adress {i}'
        #                     )
        #     client.save()

        # for i in range(1, count+1):
        #     product = Product(
        #         name=f'Product {i}',
        #         description=f'Description prpoduct{i}',
        #         price=10+i,
        #         count=i
        #     )
        #     product.save()

        for j in range(1, 3):
            for i in range(1, count+1):
                order = Order(
                    customer = Client.objects.filter(pk=i).first(),
                    total_price=i*100/2
                )
                order.save()
                order.products.set([randint(1, count)])
                
        