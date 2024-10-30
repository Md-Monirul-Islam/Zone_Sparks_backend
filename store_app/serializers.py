from rest_framework import serializers
from .models import Order, Product, Stock, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name','description','category_image']


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    class Meta:
        model = Product
        fields = ['id','name','description','price','category','product_image','category_name']


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['id','product','quantity']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id','customer','total_amount','payment_method','order_time']


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id','order','product','quantity','price','order_time']



