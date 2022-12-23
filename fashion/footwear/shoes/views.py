from datetime import date

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import *


def regview(request):
    name = request.POST['name']
    age = request.POST['age']
    image = request.FILES['image']
    address = request.POST['address']
    email = request.POST['email']
    phone = request.POST['phone']
    username = request.POST['username']
    password = request.POST['password']
    value = Register(name=name, age=age, image=image, address=address, email=email, phone=phone, username=username)
    value.save()
    value2 = Login(username=username, password=password, type=1)
    value2.save()
    return render(request, "action.html")


def action(request):
    return render(request, "action.html")


def register(request):
    return render(request, "register.html")


def index(request):
    return render(request, "index.html")


def display(request):
    return render(request, "display.html")


def check(request):
    username = request.POST['username']
    password = request.POST['password']
    value1 = Login.objects.get(username=username, password=password)
    if value1.type == 1:
        request.session['username'] = value1.username
        data3 = Product.objects.all()
        return render(request, "user.html", {'pr': data3})
    elif value1.type == 0:
        request.session['username'] = value1.username
        return render(request, "adm.html")


def login(request):
    return render(request, "login.html")


def adm(request):
    return render(request, "adm.html")


def user(request):
    return render(request, "user.html")


def userview(request):
    data = Register.objects.all()
    data1 = Login.objects.all()
    return render(request, "display.html", {'re': data, 'lo': data1})


def pro(request):
    pname = request.POST['pname']
    model = request.POST['model']
    image = request.FILES['image']
    price = request.POST['price']
    value3 = Product(pname=pname, model=model, image=image, price=price)
    value3.save()
    return render(request, "action.html")


def product(request):
    return render(request, "product.html")


def ptable(request):
    return render(request, "ptable.html")


def proview(request):
    data2 = Product.objects.all()
    return render(request, "ptable.html", {'pr': data2})


def delete(request, id):
    data4 = Product.objects.get(id=id)
    data4.delete()
    return HttpResponseRedirect(reverse("proview"))


def buy(request):
    username = request.session['username']
    pname = request.POST['pname']
    today = date.today()
    use = Register.objects.get(username=username)
    prod = Product.objects.get(id=pname)
    data5 = Buy(username=use, pname=prod, date=today)
    data5.save()
    data6 = Product.objects.all()
    return render(request, "user.html", {'pr': data6})


def show(request):
    data7 = Buy.objects.all()
    return render(request, "btable.html", {'bt': data7})


def btable(request):
    return render(request, "btable.html")


def pf(request):
    r = request.session['username']
    p = Register.objects.get(username=r)
    return render(request, "profile.html", {'re': p})


def profile(request):
    return render(request, "profile.html")


def ord(request):
    v = request.session['username']
    od = Register.objects.get(username=v)
    bd = Buy.objects.filter(username=od)
    return render(request, "ortable.html", {'or': bd})


def ortable(request):
    return render(request, "ortable.html")


def logout(request):
    return render(request, "logout.html")


def shoes(request):
    return render(request, "shoes.html")


def racingboots(request):
    return render(request, "racingboots.html")


def collection(request):
    return render(request, "collection.html")


def con(request):
    name = request.POST['name']
    phonenumber = request.POST['phonenumber']
    email = request.POST['email']
    message = request.POST['message']
    c = Contact(name=name, phonenumber=phonenumber, email=email, message=message)
    c.save()
    return render(request, "action.html")


def contact(request):
    return render(request, "contact.html")
