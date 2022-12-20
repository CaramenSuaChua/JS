from django.urls import path
from . import views
urlpatterns = [
    path('cate/', views.CategoryView.as_view()),
    path('cate/<int:pk>/', views.CategoryDetailView.as_view()),
    path('product/', views.ProductsView.as_view()),
    path('product/<int:pk>', views.ProductsDetailView.as_view())
]