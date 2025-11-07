from django.urls import path
from . import views

urlpatterns = [
path('about_me/', views.about_me, name='about_me'),
path('current_time/', views.current_time, name='current_time'),
path('phrases_random/', views.phrases_random_list, name='phrases_random')
]