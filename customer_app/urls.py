from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns = [
    path('user-profile/<int:user_id>/', views.UserProfileView.as_view(), name='user-profile'),
    path('update-user-profile/', views.UpdateUserProfileView.as_view(), name='update-user-profile'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)