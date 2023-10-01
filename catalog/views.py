from django.shortcuts import render
from catalog.models import Contacts


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(name, phone, message)

    contact = Contacts.objects.get(pk=1)
    context = {
        'object_contact': contact
    }

    return render(request, 'catalog/contacts.html', context)


def home(request):
    return render(request, 'catalog/home.html')
