from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ecommerce.models import Product


class CategoriesView(APIView):
    def get(self, request):
        categories = Product.objects.values_list('category_name', flat=True).distinct()
        return Response(categories, status=status.HTTP_200_OK)
