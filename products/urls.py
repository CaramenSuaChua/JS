
from django.urls import path
from . import views
urlpatterns = [
    path('', views.ProductsView.as_view() ),
    path('<int:pk>', views.ProductsView.as_view() ),
]