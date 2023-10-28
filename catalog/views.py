from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse

from catalog.forms import ProductForm, VersionForm, ProductFormMod
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


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:list_product')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save
        return super().form_valid(form)


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product

    def get_form_class(self):
        if self.request.user.is_staff:
            return ProductFormMod
        return ProductForm

    def get_success_url(self):
        return reverse('catalog:view_product', args=[self.object.pk])

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save
        return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:list_product')


class VersionCreateView(LoginRequiredMixin, CreateView):
    model = Version
    form_class = VersionForm

    def get_success_url(self):
        return reverse('catalog:view_product', args=[self.object.product.pk])
