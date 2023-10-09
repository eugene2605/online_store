from django.shortcuts import render
from django.views.generic import DetailView, ListView

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


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object
