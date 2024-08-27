import json

from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Basket, Invoice, Product, ProductCount
from .serializers import AddItemToBasketRequestDto, CheckoutBasketRequestDto, ProductSerializer


class BlackFridayController(viewsets.ViewSet):
    @action(detail=False, methods=['post'])
    def add_item_to_basket(self, request):
        serializer = AddItemToBasketRequestDto(data=request.data)
        serializer.is_valid(raise_exception=True)
        request_data = serializer.validated_data

        product = get_object_or_404(Product, asin=request_data['product_id'])
        item_exists = Basket.objects.filter(product_id=request_data['product_id'], basket_id=request_data['basket_id'],
                                            user_id=request_data['user_id']).exists()

        if item_exists:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        product_count = get_object_or_404(ProductCount, asin=product.asin)
        if product_count.count == 0:
            return Response("not enough items", status=status.HTTP_412_PRECONDITION_FAILED)

        Basket.objects.create(
            basket_id=request_data['basket_id'],
            user_id=request_data['user_id'],
            is_checked_out=False,
            product_id=request_data['product_id']
        )

        return Response(status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'])
    def checkout_basket(self, request):
        serializer = CheckoutBasketRequestDto(data=request.data)
        serializer.is_valid(raise_exception=True)
        request_data = serializer.validated_data

        basket_items = Basket.objects.filter(basket_id=request_data['basket_id'], user_id=request_data['user_id'],
                                             is_checked_out=False)
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

    @action(detail=False, methods=['get'])
    def categories(self, request):
        categories = Product.objects.values_list('category_name', flat=True).distinct()
        return Response(categories, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'])
    def items(self, request, pk=None):
        product = get_object_or_404(Product, asin=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'])
    def categories_items(self, request, pk=None):
        category_items = Product.objects.filter(category_name=pk)
        if not category_items.exists():
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(category_items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
