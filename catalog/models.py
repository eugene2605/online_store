from django.conf import settings
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='catalog/', null=True, blank=True, verbose_name='Изображение')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Цена за покупку')
    date_of_creation = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name='Дата создания')
    date_last_modified = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name='Дата последнего изменения')
    views_count = models.IntegerField(default=0, verbose_name='Просмотры')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='Владелец')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')

    def __str__(self):
        return f'{self.name} {self.category} {self.price}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('name',)
        permissions = [
            (
                'set_published',
                'Can publish posts'
            )
        ]


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('name',)


class Contacts(models.Model):
    country = models.CharField(max_length=50, verbose_name='Страна')
    inn = models.CharField(max_length=20, verbose_name='ИНН')
    address = models.CharField(max_length=100, verbose_name='Адрес')

    def __str__(self):
        return f'{self.country} {self.inn} {self.address}'

    class Meta:
        verbose_name = 'контакты'
        verbose_name_plural = 'контакты'


class Version(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='продукт')
    version_number = models.IntegerField(verbose_name='номер версии')
    version_name = models.CharField(max_length=100, verbose_name='название версии')
    is_active = models.BooleanField(default=True, verbose_name='текущая версия')

    def __str__(self):
        return f'{self.product} - {self.version_number} ({self.version_name})'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
