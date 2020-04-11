from django.shortcuts import render
from django.http import HttpResponse
#from accounts.models import *
from .models import Customer, Car, Order
# Create your views here.

def home(request):
    order = Order.objects.all()
    customer = Customer.objects.all()

    context =   { 
                'orders':order,
                'customers':customer,
                }

    return render(request, 'accounts/dashboard.html', context)

def products(request):
    cars = Car.objects.all()
    return render(request, 'accounts/products.html', {'cars':cars})

def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    
    orders = customer.order_set.all()
    #car_name = Car.Make()
    order_count = orders.count()
     
    context = {
        'customer': customer,
        'orders': orders,
        'order_count':order_count,
        
        #'car_name': car_name,
    }
    return render(request, 'accounts/customer.html', context)

