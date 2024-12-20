
from rest_framework import serializers
from . models import *

#::::::::  CATEGORY SERIALIZER
class CategorySerializer(serializers.ModelSeriaizer):
    class Meta:
        model = Category
        fields = '__all__'

#::::::::::::::  ProductSerializer
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class CartProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartProduct
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class CheckoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ['cart', 'amount', 'order_status', 'subtotal', 'payment_complete', 'ref']
    