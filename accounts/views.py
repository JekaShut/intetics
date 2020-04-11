from django.shortcuts import render, redirect
from django.http import HttpResponse
#from accounts.models import *
from .models import Customer, Car, Order
from .forms import OrderForm
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
    
    order_count = orders.count()
    
     
    context = {
        'customer': customer,
        'orders': orders,
        'order_count':order_count,
        
        
        
        
      
    }
    return render(request, 'accounts/customer.html', context)

def createOrder(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}

    return render(request, 'accounts/order_form.html', context)

def updateOrder(request, pk):
    
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}

    return render(request, 'accounts/order_form.html', context)

def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/')
    context = {'item':order}
    return render(request, 'accounts/delete.html', context)
