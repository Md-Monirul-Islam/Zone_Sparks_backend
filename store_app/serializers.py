from rest_framework import serializers
from .models import Order, OrderItems, Product, Stock, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name','description','category_image']


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    class Meta:
        model = Product
        fields = ['id','name','description','price','category','product_image','category_name','stock_status']


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['id','product','quantity']


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItems
        fields = ['product', 'quantity', 'price']

class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['customer', 'total_amount', 'payment_method', 'order_items']



