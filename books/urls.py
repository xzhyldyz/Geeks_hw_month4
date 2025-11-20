from django.urls import path
from . import views

urlpatterns = [
# path('about_me/', views.about_me, name='about_me'),
# # path('current_time/', views.current_time, name='current_time'),
# path('phrases_random/', views.phrases_random_list, name='phrases_random')
    path('', views.BookListView, name='book_list'),
    path('book_list/<int:id>/', views.BookDetailView, name='book_detail'),
    path('search/', views.searchView, name='search'),
]