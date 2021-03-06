from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('products/', views.products, name="products"),
    path('customer/<str:pk>', views.customer, name="customer"),
    path('create_order/', views.createOrder, name="create_order"),
    path('update_order/<str:pk>', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>', views.deleteOrder, name="delete_order"),
    path('create_customer/', views.createCustomer, name="create_customer"),
    path('customer/', views.customerSearch, name="customer_search"),
    path('update_customer/<str:pk>', views.updateCustomer, name="update_customer"),
    path('delete_customer/<str:pk>', views.deleteCustomer, name="delete_customer"),
    path('orders/', views.orders, name="orders"),
    path('create_car/', views.createCar, name="create_car"),
    path('update_car/<str:pk>', views.updateCar, name="update_car"),
    path('delete_car/<str:pk>', views.deleteCar, name="delete_car"),
    path('products_error/', views.productsError, name="products_error"),
]