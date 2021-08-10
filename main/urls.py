from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('products/<str:prod_id>', views.product_detail)
]