from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.response import Response
from .models import Category, Product, Stock
from .serializers import CategorySerializer, ProductSerializer, StockSerializer

# Create your views here.
class CategoryListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



# Update View for Category
class CategoryUpdateView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'

# Delete View for Category
class CategoryDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'


def category_count(request):
    count = Category.objects.count()
    return JsonResponse({'count': count})



class ProductListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



# Retrieve and Update a specific product
class ProductRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Delete a specific product
class ProductDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


def product_count(request):
    product = Product.objects.count()
    return JsonResponse({'product': product})



@api_view(['POST'])
# @permission_classes(IsAuthenticated)
def add_stock(request):
    if request.method == 'POST':
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity')

        print(f'Product ID: {product_id}, Quantity: {quantity}')  # Debugging line

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found.'}, status=status.HTTP_404_NOT_FOUND)

        # Create or update stock
        stock, created = Stock.objects.get_or_create(product=product)

        # Check if quantity is valid
        if quantity is None or quantity < 0:
            return Response({'error': 'Quantity must be a non-negative number.'}, status=status.HTTP_400_BAD_REQUEST)

        stock.quantity += quantity
        stock.save()

        # Serialize the updated stock for response
        serializer = StockSerializer(stock)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response({'error': 'Invalid request method.'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def search_products(request):
    query = request.GET.get('query', '')
    products = Product.objects.filter(name__icontains=query)
    product_data = [{'id': product.id, 'name': product.name} for product in products]
    return Response(product_data, status=status.HTTP_200_OK)


def process_sale(product_id, quantity_sold):
    try:
        product = Product.objects.get(id=product_id)
        stock = product.stocks.first()

        if stock is None or stock.quantity < quantity_sold:
            raise ValueError("Insufficient stock to complete the sale.")

        # Update stock quantity
        stock.quantity -= quantity_sold
        stock.save()

        # Update total sales
        product.total_sales += quantity_sold
        product.save()

        return True  # Sale processed successfully
    except Product.DoesNotExist:
        raise ValueError("Product not found.")


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def sell_product(request):
    product_id = request.data.get('product_id')
    quantity = request.data.get('quantity')

    try:
        process_sale(product_id, quantity)
        return Response({'message': 'Sale processed successfully.'}, status=status.HTTP_200_OK)
    except ValueError as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    


class StockListView(generics.ListAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


class StockListUpadeDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    
    