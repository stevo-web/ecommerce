from django.urls import path
from . import views


urlpatterns = [
    path('sell/', views.sell, name="sell"),
    path('', views.dashboard, name="shop-dashboard"),
    path('products/', views.products, name="products"),
    path('add-product/', views.add_product, name="add-product"),
    path('delete-product/<str:pk>', views.delete_product, name="delete-product"),
    # path('edit-product/<str:pk>', views.edit_product, name="edit-product")
]
