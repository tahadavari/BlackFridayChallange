from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ecommerce.models import Product, Basket, ProductCount
from ecommerce.serializers import AddItemToBasketRequestDto


class AddItemToBasketView(APIView):
    def post(self, request):
        serializer = AddItemToBasketRequestDto(data=request.data)
        serializer.is_valid(raise_exception=True)
        request_data = serializer.validated_data

        product = get_object_or_404(Product, asin=request_data['product-id'])
        item_exists = Basket.objects.filter(
            product_id=request_data['product-id'],
            basket_id=request_data['basket-id'],
            user_id=request_data['user-id']
        ).exists()

        if item_exists:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        product_count = get_object_or_404(ProductCount, asin=product.asin)
        if product_count.count == 0:
            return Response("not enough items", status=status.HTTP_412_PRECONDITION_FAILED)

        Basket.objects.create(
            basket_id=request_data['basket-id'],
            user_id=request_data['user-id'],
            is_checked_out=False,
            product_id=request_data['product-id']
        )

        return Response(status=status.HTTP_200_OK)
