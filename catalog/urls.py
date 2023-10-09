from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import contacts, home, ProductDetailView, ProductListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('catalog/', ProductListView.as_view(), name='list_student'),
    path('view/<int:pk>/', ProductDetailView.as_view(), name='view_student'),
]
