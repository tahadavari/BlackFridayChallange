from rest_framework import serializers

from .models import Basket, Invoice, Product, ProductCount


class AddItemToBasketRequestDto(serializers.Serializer):
    basket_id = serializers.CharField()
    product_id = serializers.CharField()
    user_id = serializers.CharField()

    def to_internal_value(self, data):
        # Copy data to prevent side effects
        data = data.copy()

        # Mapping 'kebab-case' keys to 'snake_case'
        data['basket_id'] = data.pop('basket-id', None)
        data['product_id'] = data.pop('product-id', None)
        data['user_id'] = data.pop('user-id', None)

        return super().to_internal_value(data)


class CheckoutBasketRequestDto(serializers.Serializer):
    basket_id = serializers.CharField()
    user_id = serializers.CharField()

    def to_internal_value(self, data):
        data = data.copy()
        data['basket_id'] = data.pop('basket-id', None)
        data['user_id'] = data.pop('user-id', None)

        return super().to_internal_value(data)


class ProductSerializer(serializers.ModelSerializer):
    asin = serializers.CharField()
    boughtInLastMonth = serializers.IntegerField(source='bought_in_last_month')
    categoryName = serializers.CharField(source='category_name')
    imgUrl = serializers.CharField(source='img_url')
    isBestSeller = serializers.BooleanField(source='is_best_seller')
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    productUrl = serializers.CharField(source='product_url')
    reviews = serializers.IntegerField()
    stars = serializers.DecimalField(max_digits=3, decimal_places=1)
    title = serializers.CharField()

    class Meta:
        model = Product
        fields = ['asin', 'boughtInLastMonth', 'categoryName', 'imgUrl', 'isBestSeller', 'price', 'productUrl', 'reviews', 'stars', 'title']


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
