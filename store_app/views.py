from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics
from .models import Category
from .serializers import CategorySerializer

# Create your views here.
class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer