
from django.urls import path
from . import views
urlpatterns = [
    path('order/', views.OrderView.as_view()),
    path('order/<int:pk>/', views.OrderDetailView.as_view()),
    path('order_item/', views.OrderItemView.as_view()),
    path('order_item/<int:pk>/', views.OrderItemDView.as_view())
]