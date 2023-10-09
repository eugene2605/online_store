from django.urls import path
from blog.apps import BlogConfig
from blog.views import *

app_name = BlogConfig.name

urlpatterns = [
    path('', BlogListView.as_view(), name='list_blog'),
    path('create/', BlogCreateView.as_view(), name='create_blog'),
    path('view/<int:pk>/', BlogDetailView.as_view(), name='view_blog'),
    path('edit/<int:pk>/', BlogUpdateView.as_view(), name='edit_blog'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete_blog'),
]
