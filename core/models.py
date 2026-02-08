from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    specs = models.TextField(blank=True)

    def __str__(self):
        return self.name


STATUS_CHOICES = [
    ("new", "جديد"),
    ("contacted", "تم التواصل"),
    ("closed", "مغلق"),
]


class QuoteRequest(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="requests")
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=40)
    email = models.EmailField(blank=True)
    company = models.CharField(max_length=160, blank=True)
    message = models.TextField(blank=True)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="new")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.product.slug}"
