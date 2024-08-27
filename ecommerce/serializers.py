from rest_framework import serializers

from .models import Basket, Invoice, Product, ProductCount


class AddItemToBasketRequestDto(serializers.Serializer):
    basket_id = serializers.CharField()
    product_id = serializers.CharField()
    user_id = serializers.CharField()


class CheckoutBasketRequestDto(serializers.Serializer):
    basket_id = serializers.CharField()
    user_id = serializers.CharField()


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
