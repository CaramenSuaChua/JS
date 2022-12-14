from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

urlpatterns = [
    path('api/register/', views.RegisterView.as_view(), name='register'),
    path('api/login', views.LoginView.as_view(), name='login'),
    path('api/logout', views.LogoutView.as_view(), name='logout'),
    path('api/user', views.UserRetrieveUpdateAPIView.as_view(), name='user'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]