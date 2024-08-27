import json

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ecommerce.models import Basket, ProductCount, Invoice
from ecommerce.serializers import CheckoutBasketRequestDto


class CheckoutBasketView(APIView):
    def post(self, request):
        serializer = CheckoutBasketRequestDto(data=request.data)
        serializer.is_valid(raise_exception=True)
        request_data = serializer.validated_data

        basket_items = Basket.objects.filter(
            basket_id=request_data['basket_id'],
            user_id=request_data['user_id'],
            is_checked_out=False
        )
        if not basket_items.exists():
            return Response(status=status.HTTP_404_NOT_FOUND)

        item_counts = {}
        for item in basket_items:
            product_count = get_object_or_404(ProductCount, asin=item.product_id)
            if product_count.count == 0:
                return Response("not enough items", status=status.HTTP_412_PRECONDITION_FAILED)
            item_counts[item.product_id] = product_count

        for item in basket_items:
            item.is_checked_out = True
            item_counts[item.product_id].count -= 1
            item.save()
            item_counts[item.product_id].save()

        items_json = json.dumps([item.product_id for item in basket_items])
        Invoice.objects.create(
            basket_id=request_data['basket_id'],
            user_id=request_data['user_id'],
            items=items_json
        )

        return Response(status=status.HTTP_200_OK)
