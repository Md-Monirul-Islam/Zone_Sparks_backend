from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns = [
    path('products-show-in-hoem-page/', views.ProductListCreateView.as_view(), name='products-show-in-hoem-page'),
    path('product-detail/<int:product_id>/', views.product_detail, name='product-detail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)