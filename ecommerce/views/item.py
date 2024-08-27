from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ecommerce.models import Product
from ecommerce.serializers import ProductSerializer


class ItemsView(APIView):
    def get(self, request, pk=None):
        product = get_object_or_404(Product, asin=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
