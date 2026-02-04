from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework import status

from .models import Product, QuoteRequest
from .serializers import ProductSerializer, QuoteRequestSerializer, QuoteListSerializer


@api_view(["GET"])
@permission_classes([AllowAny])
def health(request):
    return Response({"ok": True, "service": "Royal Steel API"})


@api_view(["GET"])
@permission_classes([AllowAny])
def product_list(request):
    qs = Product.objects.all().order_by("name")
    return Response(ProductSerializer(qs, many=True).data)


@api_view(["POST"])
@permission_classes([AllowAny])
def create_quote(request):
    """
    يستقبل طلب عرض سعر من الفرونت:
    {
      product_slug, name, phone, email?, company?, message?
    }
    """
    serializer = QuoteRequestSerializer(data=request.data)
    if serializer.is_valid():
        obj = serializer.save()
        return Response({"ok": True, "id": obj.id}, status=status.HTTP_201_CREATED)

    return Response({"ok": False, "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([IsAdminUser])
def admin_quotes(request):
    qs = QuoteRequest.objects.select_related("product").order_by("-created_at")[:300]
    return Response({"ok": True, "items": QuoteListSerializer(qs, many=True).data})

