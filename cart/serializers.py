from rest_framework import serializers
from cart.models import Cart,Cart_items
from groceries.serializers import ProductSerializer

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('id', 'title', 'price', 'time_created', 'time_completed', 'total')

class Cart_itemsSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    cart = CartSerializer(read_only=True)

    class Meta:
        model = Cart_items
        fields = ('id', 'cart', 'product', 'quantity')
