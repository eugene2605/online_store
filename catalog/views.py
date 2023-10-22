from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Contacts, Product, Version


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


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:list_product')


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm


    def get_success_url(self):
        from django.urls import reverse
        return reverse('catalog:view_product', args=[self.object.pk])


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:list_product')


class VersionCreateView(CreateView):
    model = Version
    form_class = VersionForm

    def get_success_url(self):
        from django.urls import reverse
        return reverse('catalog:view_product', args=[self.object.product.pk])
