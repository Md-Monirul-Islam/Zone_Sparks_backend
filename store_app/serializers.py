from rest_framework import serializers
from .models import Product, Stock, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name','description','category_image']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','name','description','price','category','product_image']


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['id','product','quantity']



