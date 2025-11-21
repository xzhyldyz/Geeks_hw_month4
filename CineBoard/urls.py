from django.urls import path
from . import views

urlpatterns = [
    path('add_film/', views.CreateFilmView.as_view(), name='add_film'),
    path('films/', views.FilmListView.as_view(), name='film_list'),
    path('films/<int:id>/update/', views.FilmUpdateView.as_view(), name='film_update'),
    path('films/<int:id>/delete/', views.FilmDeletView.as_view(), name='film_delete'),
    path('film/search/', views.SearchView.as_view(), name='film_search'),

    path('register/', views.ReqisterView.as_view(), name='cine_register'),
    path('login/', views.AuthLoginView.as_view(), name='cine_login'),
    path('logout/', views.AuthLoginView.as_view(), name='cine_logout'),

    path('films/cartoon/', views.cartoonFilmView, name='cartoon_films'),
    path('films/cinema/', views.cinemaFilmsView, name='cinema_films'),
]