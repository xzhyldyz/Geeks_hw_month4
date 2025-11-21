from django.shortcuts import render, redirect, get_object_or_404
from .forms import FilmForm
from . import models
from django.views import generic

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.views import View


class CreateFilmView(generic.CreateView):
    model = models.Film
    form_class = FilmForm
    template_name = 'cineboard/film_create.html'
    success_url = '/films/'

# def createFilm(request):
#     if request.method == 'POST':
#         form = FilmForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('film_list')
#     else:
#         form = FilmForm()
#     return render(request, 'cineboard/film_create.html', {'form': form})


class FilmListView(generic.ListView):
    template_name = 'cineboard/film_list.html'
    model = models.Film
    context_object_name = 'films'
    ordering = ['-id']


class FilmUpdateView(generic.UpdateView):
    model = models.Film
    form_class = FilmForm
    template_name = 'cineboard/film_update.html'
    success_url = '/films/'

    def get_object(self, **kwargs):
        todo_id = self.kwargs.get('id')
        return get_object_or_404(models.Film, id=todo_id)
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super(FilmUpdateView, self).form_valid(form=form)


# def updateFilm(request, id):
#     film = get_object_or_404(models.Film, id=id)

#     if request.method == 'POST':
#         form = FilmForm(request.POST, request.FILES, instance=film)
#         if form.is_valid():
#             form.save()
#             return redirect('film_list')
#     else:
#         form = FilmForm(instance=film)
#     return render(request, 'cineboard/film_update.html', {'form': form})


# def deleteFilm(request, id):
#     film = get_object_or_404(models.Film, id=id)
#     if request.method == 'POST':
#         film.delete()
#         return redirect('film_list')
#     return render(request, 'cineboard/film_delete.html', {'film': film})

# def searchFilmView(request):
#     query = request.GET.get('s', '')
#     films = models.Film.objects.filter(title__icontains=query) if query else models.Film.none
#     context = {
#         'films':films,
#         's': query,
#     }
#     return render(request, template_name='cineboard/film_list.html', context=context)

class FilmDeletView(generic.DeleteView):
    model = models.Film
    template_name = 'cineboard/film_delete.html'
    success_url = '/films/'
    pk_url_kwarg = 'id'



class SearchView(generic.View):
    def get(self, request):
        query = request.GET.get('s', '')
        if query:
            film = models.Film.objects.filter(title__icontains=query)
        else:
            film = models.Film.objects.none
        context = {
            'film': film,
            's': query
        }
        return render(request, template_name='tvShow/films.html', context=context)


# ------------------------------------------------------------------------------
#REGISTER
class ReqisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'cineboard/register.html', {"form": form})
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
        return render(request, 'cineboard/register.html', {"form": form})

#LOGIN
class AuthLoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'cineboard/login.html', {"form": form})
    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("users:user_list")
        return render(request, 'cineboard/login.html', {'form': form})
    
class AuthLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("film_list")
    


# ------------------------------------------------------------------------------------------

#Кино
def cinemaFilmsView(request):
    if request.method == "GET":
        films = models.Film.objects.filter(tags__name='кино')
        return render(request, 'cineboard/film_list.html', {'films':films })
    

#Мультфильмы
def cartoonFilmView(request):
    if request.method == "GET":
        films = models.Film.objects.filter(tags__name='#Мультфильмы')
        return render(request, 'cineboard/film_list.html', {'films': films})