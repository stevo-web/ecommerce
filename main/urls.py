from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('products/<str:prod_id>', views.product_detail, name="products"),
    path('category/<str:cat_id>', views.category, name="category"),
    path('search', views.search, name="search"),
    path('cart/', views.cart_list, name="cart"),
    path('cart/add/<str:prod_id>/<str:quantity>', views.add_cart, name="add-cart"),
    path('cart/remove/<str:prod_id>', views.remove, name='remove'),
    path('cart/update_plus/<str:prod_id>/<str:quantity>', views.update_plus, name='update_plus'),
    path('cart/update_minus/<str:prod_id>/<str:quantity>', views.update_minus, name='update_minus'),
    path('checkout/', views.checkout, name='checkout')
]
