from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('products/<str:prod_id>', views.product_detail, name="products"),
    path('cart/', views.cart_list, name="cart"),
    path('cart/api', views.cart_api, name="cart_api"),
    path('cart/add-item/<str:prod_id>/<str:quantity>', views.add_to_cart, name="add_to_cart")
]
