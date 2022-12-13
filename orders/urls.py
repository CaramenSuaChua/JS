
from django.urls import path
from . import views
urlpatterns = [
    path('', views.OrdersView.as_view()),
    path('<int:pk>', views.OrderDetailView.as_view()),

]
