from django.shortcuts import render, redirect
from django.http import HttpResponse
#from accounts.models import *
from .models import Customer, Car, Order
from .forms import OrderForm, CustomerForm
from .filters import OrderFilter, CustomerFilter
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

    context = {
            'cars':cars,
            
    }

    return render(request, 'accounts/products.html', context)

def orders(request):
    order = Order.objects.all()

    orderFilter = OrderFilter(request.GET, queryset=order)
    order = orderFilter.qs

    context = {
            'orders' : order,
            'orderFilter': orderFilter,
            'customers': customer,
    }
    return render(request, 'accounts/orders.html', context)


def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    order_count = orders.count()

    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs



    context = {
        'customer': customer,
        'orders': orders,
        'order_count': order_count,
        'myFilter': myFilter,
    }
    return render(request, 'accounts/customer.html', context)

def customerSearch(request):
    customer = Customer.objects.all()

    customerFilter = CustomerFilter(request.GET, queryset=customer)
    customer = customerFilter.qs

    context = { 
               'customers':customer,
               'customerFilter': customerFilter,
        }
    return render(request, 'accounts/customer_search.html', context)

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

def createCustomer(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'accounts/customer_form.html', context)

def updateCustomer(request, pk):
    
    customer = Customer.objects.get(id=pk)
    form = CustomerForm(instance=customer)# передает значения в форму
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)# передает значения в форму
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}

    return render(request, 'accounts/customer_form.html', context)


def deleteCustomer(request, pk):
    сustomerDel = Customer.objects.get(id=pk)
    if request.method == "POST":
        сustomerDel.delete()
        return redirect('/')
    context = {'item':сustomerDel}
    return render(request, 'accounts/delete_customer.html', context)


