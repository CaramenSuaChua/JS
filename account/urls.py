from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

urlpatterns = [
    path('register/', views.UsersView.as_view(), name='register'),
    path('login/', views.ObtainTokenPairWithColorView.as_view(), name='login'),
    path('refresh/', views.DecoratedTokenRefreshView.as_view(), name='logout'),
]