import django_filters

from .models import *

class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Order
        fields = ['car']

class CustomerFilter(django_filters.FilterSet):
    class Meta:
        model = Customer
        fields = ['first_name','last_name', 'phone', 'email']

class OrdersFilter(django_filters.FilterSet):
    class Meta:
        model = Order
        fields = ['car']