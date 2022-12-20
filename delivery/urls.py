from django.urls import path

#import views
from . import views
urlpatterns = [
    path('deli_unit/', views.DeliveryUnitView.as_view()),
    path('deli_unit/<int:pk>/', views.DeliveryUnitDetailView.as_view()),
    path('deli/', views.DeliveryView.as_view()),
    path('deli/<int:pk>/', views.DeliveryDetailView.as_view()),
  
]