from django.urls import path
from .views import health, product_list, create_quote, admin_quotes

urlpatterns = [
    path("health/", health),
    path("products/", product_list),
    path("quotes/", create_quote),
    path("admin/quotes/", admin_quotes),
]
