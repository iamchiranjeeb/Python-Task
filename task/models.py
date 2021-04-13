from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
# Create your models here.

class Employees(models.Model):
    firstName = models.CharField(max_length=30,null=True)
    middleName = models.CharField(max_length=30,null=False)
    lastName = models.CharField(max_length=30,null=True)
    email = models.EmailField(max_length=50,null=False)
    phone = PhoneNumberField(null=True)
    DOB = models.DateField(null=False)

    def __str__(self):
        return self.firstName
    
class EmployeeTable(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    phone = PhoneNumberField()
    DOB = models.DateField()


    def __str__(self):
        return self.firstName


class EmployeesTable(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    phone = PhoneNumberField()
    DOB = models.DateField()
    img = models.ImageField(upload_to='images/%Y/%m/%d/',default='default.jpg')
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.firstName