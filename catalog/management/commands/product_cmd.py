from django.core.management import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        product_list = [
            {
                'name': 'диван',
                'description': 'None',
                'category': Category.objects.get(name='мягкая мебель'),
                'price': '45000'
            },
            {
                'name': 'кресло',
                'description': 'None',
                'category': Category.objects.get(name='мягкая мебель'),
                'price': '13000'
            },
            {
                'name': 'конкурент',
                'description': 'легендарная настольная игра в обновленном дизайне',
                'category': Category.objects.get(name='игрушки'),
                'price': '2700'
            },
            {
                'name': 'дартс',
                'description': 'если хочешь научиться всегда попадать в цель',
                'category': Category.objects.get(name='игрушки'),
                'price': '1500'
            },
            {
                'name': 'перфоратор',
                'description': 'сверлит бетон как по маслу',
                'category': Category.objects.get(name='электроинструмент'),
                'price': '5200'
            },
            {
                'name': 'электролобзик',
                'description': 'легко идет даже по сложной траектории',
                'category': Category.objects.get(name='электроинструмент'),
                'price': '7600'
            },
        ]

        product_for_create = []
        for product_item in product_list:
            product_for_create.append(Product(**product_item))

        Product.objects.all().delete()
        Product.objects.bulk_create(product_for_create)
