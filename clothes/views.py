from django.shortcuts import render
from . import models


#Все товары
def all_products(request):
   if request.method == "GET":
      products = models.Products.objects.all()
      return render(request, 'clothes/all_products.html', {'products':products })


#Женское
def womanProductsView(request):
    if request.method == "GET":
        woman_products = models.Products.objects.filter(tags__name='#женский')
        return render(request, 'clothes/woman_products.html', {'woman_products': woman_products})
    
#Мужское
def manProductsView(request):
    if request.method == "GET":
        man_products = models.Products.objects.filter(tags__name='#мужской')
        return render(request, 'clothes/man_products.html', {'man_products': man_products})
    

#Детское
def kidProductsView(request):
    if request.method == "GET":
        kid_products = models.Products.objects.filter(tags__name='#детский')
        return render(request, 'clothes/kid_products.html', {'kid_products': kid_products})
    

#Для подростков
def teenagerProductsView(request):
    if request.method == "GET":
        teenager_products = models.Products.objects.filter(tags__name='#для подростков')
        return render(request, 'clothes/teenager_products.html', {'teenager_products': teenager_products})
    

#Уни
def uniProductsView(request):
    if request.method == "GET":
        uni_products = models.Products.objects.filter(tags__name='#Unisex')
        return render(request, 'clothes/uni_products.html', {'uni_products': uni_products})