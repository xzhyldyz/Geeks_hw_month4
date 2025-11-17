from django.urls import path
from . import views

urlpatterns = [
    path('basket/create/<int:id>/', views.createOrderView, name='basket_create'),
    path('basket/', views.basketListView, name='basket_list'),
    path('basket/delete/<int:id>/', views.deleteOrderView, name = 'basket_delete')
]