from django.contrib import admin
from catalog.models import Product, Category, Contacts


# При этом интерфейс вывода продуктов настройте так, чтобы можно было результат отображения фильтровать по категории,
# а также осуществлять поиск по названию и полю описания.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'description')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('name',)
    search_fields = ('name', 'description')


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('id', 'country', 'inn', 'address')
