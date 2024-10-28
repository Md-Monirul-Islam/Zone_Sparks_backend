from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns = [
    path('categories/', views.CategoryListCreateAPIView.as_view(), name='category-list-create'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
