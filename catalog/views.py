from django.shortcuts import render
from catalog.models import Contacts, Product


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(name, phone, message)

    contact = Contacts.objects.get(pk=1)
    context = {
        'object_contact': contact,
        'title': 'Контакты'
    }

    return render(request, 'catalog/contacts.html', context)


def home(request):

    context = {
        'title': 'Skystore'
    }

    return render(request, 'catalog/home.html', context)


def catalog(request):

    product_list = Product.objects.all()
    context = {
        'object_list': product_list,
        'title': 'Каталог'
    }

    return render(request, 'catalog/catalog.html', context)
