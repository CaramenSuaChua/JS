from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

urlpatterns = [
    path('api/register/', views.UsersView.as_view(), name='register'),
    path('api/login/', views.ObtainTokenPairWithColorView.as_view(), name='login'),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/refresh/', views.DecoratedTokenRefreshView.as_view(), name='logout'),
    # path('api/user', views.ProfileView.as_view(), name='user'),
]