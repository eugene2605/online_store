from django.core.management import BaseCommand
from catalog.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        category_list = [
            {'name': 'мягкая мебель', 'description': 'лучшие вещи для пассивного отдыха'},
            {'name': 'игрушки', 'description': 'все для приятного и полезного досуга'},
            {'name': 'электроинструмент', 'description': 'с ними любой ремонт - сплошное удовольствие'}
        ]

        category_for_create = []
        for category_item in category_list:
            category_for_create.append(Category(**category_item))

        Category.objects.all().delete()
        Category.objects.bulk_create(category_for_create)
