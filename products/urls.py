from django.urls import path
from .views import *

urlpatterns = [
    path('getinfo/', get_info, name='home'),
    path('create/', create_product, name='create'),
    path('detail/<int:pk>/', detail_product, name='product_detail'),
    path('updateproduct/<int:pk>/', update_product, name='updateproduct'),
    path('deleteproduct/<int:pk>/', delete_product, name='deleteproduct')
]