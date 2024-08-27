from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ecommerce.models import Product
from ecommerce.serializers import ProductSerializer


class CategoriesItemsView(APIView):
    def get(self, request, pk=None):
        category_items = Product.objects.filter(category_name=pk)
        if not category_items.exists():
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(category_items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
