from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=64, null=True)
    last_name = models.CharField(max_length=64, null=True)
    date_of_birth = models.DateTimeField(null=True)
    adress = models.CharField(max_length=64, null=True)
    phone = models.CharField(max_length=64, null=True)
    email = models.EmailField(max_length=64, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.first_name) + " " + str(self.last_name)

class Car(models.Model):
    Make = models.CharField(max_length=64, null=True)
    Model = models.CharField(max_length=64, null=True)
    Year = models.CharField(max_length=64, null=True)
    VIN = models.CharField(max_length=64, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.Make) + " " + str(self.Model)

    


class Order(models.Model):
    STATUS = (
        ('Completed', 'Completed'),
        ('In Progress', 'In Progress'),
        ('Cancelled', 'Cancelled')
    )
    
    car = models.ForeignKey(Car, null=True, on_delete=models.SET_NULL)
    date = models.DateTimeField(auto_now_add=True, null=True)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    Order_amount = models.FloatField(max_length=64, null=True,validators=[MinValueValidator(1), MaxValueValidator(10000)])
    Order_status = models.CharField(max_length=64, null=True, choices=STATUS)

    def __str__(self):
        return self.car.Make + " " + self.car.Model


