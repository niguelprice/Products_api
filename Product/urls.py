from django.urls import path
from . import views

urlpatterns = [
    path('', views.Products_list),
    path('<int:pk>/', views.Product_detail)
]