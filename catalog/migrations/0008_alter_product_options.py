# Generated by Django 4.2.5 on 2023-10-26 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_product_is_published_alter_product_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('name',), 'permissions': [('set_published', 'Can publish posts')], 'verbose_name': 'продукт', 'verbose_name_plural': 'продукты'},
        ),
    ]
