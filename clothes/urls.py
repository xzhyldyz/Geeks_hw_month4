from django.urls import path
from . import views

urlpatterns = [
    path('all_products/', views.all_products, name='all_prod'),
    path('woman_products/', views.womanProductsView, name='woman'),
    path('man_products/', views.manProductsView, name='man'),
    path('kid_products/', views.kidProductsView, name='kid'),
    path('teenager_products/', views.teenagerProductsView, name='teenager'),
    path('uni_products/', views.uniProductsView, name='uni'),
]