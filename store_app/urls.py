from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns = [
    path('categories/', views.CategoryListCreateAPIView.as_view(), name='category-list-create'),

    path('category/update/<int:id>/', views.CategoryUpdateView.as_view(), name='category-update'),

    path('category/delete/<int:id>/', views.CategoryDeleteView.as_view(), name='category-delete'),

    path('category-count/', views.category_count, name='category_count'),

    path('products/', views.ProductListCreateView.as_view(), name='product-list-create'),

    path('products/<int:pk>/', views.ProductRetrieveUpdateView.as_view(), name='product_retrieve_update'),

    path('products/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product_delete'),

    path('product-count/', views.product_count, name='product_count'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
