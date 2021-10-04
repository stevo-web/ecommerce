from django.urls import path
from . import views


urlpatterns = [
    path('sell/', views.sell, name="sell"),
    path('', views.dashboard, name="shop-dashboard"),
    path('orders/', views.shop_orders, name="shop-orders"),
    path('orders/<str:pk>/', views.order_detail, name="order-detail"),
    path('customers/', views.customers, name="shop-customers"),
    path('products/', views.products, name="shop-products"),
    path('add-product/', views.add_product, name="add-product"),
    path('delete-product/<str:pk>', views.delete_product, name="delete-product"),
    # path('edit-product/<str:pk>', views.edit_product, name="edit-product")
]
