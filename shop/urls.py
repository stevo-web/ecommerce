from django.urls import path
from . import views


urlpatterns = [
    path('create-shop/', views.create_shop, name="create-shop"),
    path('shop-dashboard/', views.dashboard, name="shop-dashboard")
]