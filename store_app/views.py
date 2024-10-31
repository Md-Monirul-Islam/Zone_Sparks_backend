from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer

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