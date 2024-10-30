from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics
from django.http import JsonResponse
from .models import Category
from .serializers import CategorySerializer

# Create your views here.
class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



# Update View for Category
class CategoryUpdateView(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'

# Delete View for Category
class CategoryDeleteView(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'


def category_count(request):
    count = Category.objects.count()
    return JsonResponse({'count': count})