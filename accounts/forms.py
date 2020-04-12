from django.forms import ModelForm
from .models import Order, Customer, Car
from django.core.exceptions import ValidationError

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'



class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
