from django.db import models


class Register(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    image = models.FileField()
    address = models.CharField(max_length=50)
    email = models.CharField(max_length=40)
    phone = models.IntegerField()
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=10)


class Login(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=10)
    type = models.IntegerField()


class Product(models.Model):
    pname = models.CharField(max_length=30)
    model = models.IntegerField()
    image = models.FileField()
    price = models.IntegerField()


class Buy(models.Model):
    username = models.ForeignKey(Register, on_delete=models.CASCADE)
    pname = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.CharField(max_length=25)


class Contact(models.Model):
    name = models.CharField(max_length=20)
    phonenumber = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    message = models.CharField(max_length=40)
