from rest_framework import serializers
from .models import Product, QuoteRequest


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "slug", "name", "description", "specs"]


class QuoteRequestCreateSerializer(serializers.ModelSerializer):
    product_slug = serializers.SlugField(write_only=True)

    class Meta:
        model = QuoteRequest
        fields = ["id", "product_slug", "name", "phone", "email", "company", "message", "status", "created_at"]
        read_only_fields = ["id", "status", "created_at"]

    def validate_phone(self, value):
        v = value.strip()
        if len(v) < 8:
            raise serializers.ValidationError("رقم الموبايل قصير جدًا.")
        return v

    def create(self, validated_data):
        slug = validated_data.pop("product_slug")
        try:
            product = Product.objects.get(slug=slug)
        except Product.DoesNotExist:
            raise serializers.ValidationError({"product_slug": "المنتج غير موجود."})

        return QuoteRequest.objects.create(product=product, **validated_data)


class QuoteListSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = QuoteRequest
        fields = ["id", "product", "name", "phone", "email", "company", "message", "status", "created_at"]
