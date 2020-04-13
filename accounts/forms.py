from django.forms import ModelForm
from .models import Order, Customer, Car
from django.core.exceptions import ValidationError
from django import forms

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        wigets = {
            
            
            'car': forms.TextInput(attrs={'class': 'select'}),
        }



class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        wigets = {
            'date_of_birth': forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'})
        }

class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
