from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('products/<int:client_id>/<int:count_days>', views.products, name='products'),
    path('add_product/', views.add_product, name='add_product')
]