from django.urls import path
from . import views

urlpatterns = [
    path("catalog",views.catalog, name = "catalog"),
    path("products/<int:id>/",views.products, name = "products"),
    path("product/<int:ids>/",views.product_car, name = "product_car"),


]
