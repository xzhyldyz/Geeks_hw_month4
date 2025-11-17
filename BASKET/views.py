from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms
from books.models import Book

#CRUD
def basketListView(request):
    if request.method == 'GET': 
        orders = models.Order.objects.all().order_by('-id')
    return render(request, 'basket/basket_list.html', {'orders': orders})

#CREATE ORDER
def createOrderView(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        form = forms.BasketForm(request.POST)
        if form.is_valid:
            order = form.save(commit=False)
            order.book = book
            order.save()
            return redirect('basket_list')
    else:
        form = forms.BasketForm()

    return render(request, 'basket/basket_order_create.html', {'form': form, 'book':book} )

#DELETE ORDER
def deleteOrderView(request, id):
    book = get_object_or_404(models.Order, id=id)
    if request.method == "POST":
        book.delete()
        return redirect('basket_list')
    return render(request, 'basket/basket_order_delete.html', {'book': book})