from rest_framework import serializers

from .models import Basket, Invoice, Product, ProductCount


class AddItemToBasketRequestDto(serializers.Serializer):
    basket_id = serializers.CharField(source='basket-id')
    product_id = serializers.CharField(source='product-id')
    user_id = serializers.CharField(source='user-id')


class CheckoutBasketRequestDto(serializers.Serializer):
    basket_id = serializers.CharField(source='basket-id')
    user_id = serializers.CharField(source='user-id')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = '__all__'


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'


class ProductCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCount
        fields = '__all__'
