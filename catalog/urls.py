from django.contrib.auth.decorators import login_required
from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import *

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('catalog/', ProductListView.as_view(), name='list_product'),
    path('catalog/create/', ProductCreateView.as_view(), name='create_product'),
    path('catalog/view/<int:pk>/', ProductDetailView.as_view(), name='view_product'),
    path('catalog/edit/<int:pk>/', ProductUpdateView.as_view(), name='edit_product'),
    path('catalog/delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
    # path('catalog/version/<int:pk>/', VersionUpdateView.as_view(), name='version_product'),
    path('catalog/version_create/', VersionCreateView.as_view(), name='version_create')
]
