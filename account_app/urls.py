from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views
from rest_framework import routers

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
