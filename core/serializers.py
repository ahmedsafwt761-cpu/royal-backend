from rest_framework import serializers
from .models import Product, QuoteRequest


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "slug", "name"]  # لو عندك short_desc ضيفه هنا


class QuoteRequestSerializer(serializers.ModelSerializer):
    # هنستقبل slug من الفرونت
    product_slug = serializers.SlugField(write_only=True)

    class Meta:
        model = QuoteRequest
        fields = [
            "id",
            "product_slug",
            "name",
            "phone",
            "email",
            "company",
            "message",
            "status",
            "created_at",
        ]
        read_only_fields = ["id", "status", "created_at"]

    def create(self, validated_data):
        slug = validated_data.pop("product_slug")

        try:
            product = Product.objects.get(slug=slug)
        except Product.DoesNotExist:
            # بدل 500 هيرجع 400 برسالة واضحة
            raise serializers.ValidationError(
                {"product_slug": "المنتج غير موجود. تأكد أن الـ slug موجود في Admin → Products."}
            )

        return QuoteRequest.objects.create(product=product, **validated_data)


class QuoteListSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = QuoteRequest
        fields = ["id", "slug", "name", "short_desc"]
