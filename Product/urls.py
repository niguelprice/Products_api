from django.urls import path
from . import views

urlpatterns = [
    path('', views.Products_list),
]