from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

urlpatterns = [
    path('register/', views.UsersView.as_view(), name='register'),
    path('email-verify/<uidb64>/<otp>/', views.VerifyEmail.as_view(), name='email-verify'),
    # path('email-verify/', views.VerifyEmail.as_view(), name='email-verify'),
    path('login/', views.ObtainTokenPairWithColorView.as_view(), name='login'),
    path('change-pwd/', views.ChangePasswordView.as_view(), name='change-pwd'),
    path('refresh/', views.DecoratedTokenRefreshView.as_view(), name='logout'),
     path('request-reset-email/', views.RequestPasswordResetEmail.as_view(),
         name="request-reset-email"),
    path('password-reset-confirm/<uidb64>/<otp>/',
         views.PasswordCheckTokenAPI.as_view(), name='password-reset-confirm'),
    path('password-reset-complete', views.SetNewPasswordAPIView.as_view(),
         name='password-reset-complete')
]