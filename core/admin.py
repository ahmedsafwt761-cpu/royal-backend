from django.contrib import admin
from .models import Quote


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'product_slug', 'status', 'created_at']
    list_filter = ['status', 'product_slug', 'created_at']
    search_fields = ['name', 'phone', 'email', 'message']
    readonly_fields = ['created_at', 'updated_at']
    list_editable = ['status']
    date_hierarchy = 'created_at'