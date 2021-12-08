from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from shopApp import views


urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('user/<int:pk>/', views.UserDetailView.as_view()),
    path('user/create/', views.UserCreateView.as_view()),
    path('user/update/<int:pk>/', views.UserDetailView.as_view()),
    path('user/delete/<int:pk>/', views.UserDetailView.as_view()),
    path('products/list/', views.ProductListView.as_view()),
    path('product/<int:pk>/', views.ProductDetailView.as_view()),
    path('product/create/', views.ProductCreateView.as_view()),
    path('product/update/<int:pk>/', views.ProductDetailView.as_view()),
    path('product/delete/<int:pk>/', views.ProductDetailView.as_view()),
    path('bills/list/', views.BillListView.as_view()),
    path('bill/<int:pk>/', views.BillDetailView.as_view()),
    path('bill/create/', views.BillCreateView.as_view()),
    path('bill/update/<int:pk>/', views.BillDetailView.as_view()),
    path('bill/delete/<int:pk>/', views.BillDetailView.as_view()),
    path('sales/list/', views.SaleListView.as_view()),
    path('sale/<int:pk>/', views.SaleDetailView.as_view()),
    path('sale/create/', views.SaleCreateView.as_view()),
    path('sale/update/<int:pk>/', views.SaleDetailView.as_view()),
    path('sale/delete/<int:pk>/', views.SaleDetailView.as_view()),
]
