from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('user/register/', views.registerView, name='register'),
    path('user/login/', views.authloginView, name='login'),
    path('user/logout/', views.authlogoutView, name='logout'),
    path('user_list/', views.user_list_view, name='user_list'),

]