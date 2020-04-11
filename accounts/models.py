from django.db import models

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=64, null=True)
    last_name = models.CharField(max_length=64, null=True)
    date_of_birth = models.DateTimeField(null=True)
    adress = models.CharField(max_length=64, null=True)
    phone = models.CharField(max_length=64, null=True)
    email = models.CharField(max_length=64, null=True)
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
        return str(self.Make) + str(self.Model)
    
    

class Order(models.Model):
    STATUS = (
        ('Completed', 'Completed'),
        ('In Progress', 'In Progress'),
        ('Cancelled', 'Cancelled')
    )
    
    car = models.ForeignKey(Car, null=True, on_delete=models.SET_NULL)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    Date = models.DateTimeField(null=True)
    Order_amount = models.FloatField(max_length=64, null=True)
    Order_status = models.CharField(max_length=64, null=True, choices=STATUS)


    def __str__(self):
        return str(self.Order_amount) + " " + str(self.Order_status)
