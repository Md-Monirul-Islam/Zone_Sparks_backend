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
    product_name = serializers.CharField(source='product.name', read_only=True)
    product_price = serializers.DecimalField(source='product.price', max_digits=10, decimal_places=2, read_only=True)
    stock_status = serializers.SerializerMethodField()  # Use SerializerMethodField to get stock status
    total_sales = serializers.SerializerMethodField()
    class Meta:
        model = Stock
        fields = ['id','product','quantity','product_price','product_name','stock_status','total_sales']

    def get_stock_status(self, obj):
        # Access the stock status from the related Product model
        return obj.product.stock_status()
    
    def get_total_sales(self, obj):
        # Calculate total sales from the OrderItems model associated with the product
        return obj.product.get_total_sales()


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItems
        fields = ['product', 'quantity', 'price']

class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['customer', 'total_amount', 'payment_method', 'order_items']



