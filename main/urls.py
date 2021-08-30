from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('products/<str:prod_id>', views.product_detail, name="products"),
    path('category/<str:cat_id>', views.category, name="category"),
    path('search', views.search, name="search"),
    path('cart/', views.cart_list, name="cart"),
    path('checkout/', views.checkout, name='checkout')
]
