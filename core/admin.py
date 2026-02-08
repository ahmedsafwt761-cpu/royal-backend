from django.contrib import admin
from .models import Product, QuoteRequest


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(QuoteRequest)
class QuoteRequestAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "product", "status", "created_at")
    list_filter = ("status", "created_at", "product")
    search_fields = ("name", "phone", "email", "company", "message", "product__name", "product__slug")
    ordering = ("-created_at",)
