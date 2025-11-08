from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
# from datetime import datetime as dt
# import random
from . import models

def BookListView(request):
    if request.method == 'GET':
        book = models.Book.objects.all()
        context = {
            'book': book
        }
    return render(request, template_name='books/books.html', context=context)


def BookDetailView(request, id):
    if request.method == 'GET':
        book_id = get_object_or_404(models.Book, id=id)
        context = {
            'book_id': book_id
        }
    return render(request, template_name='books/book_detail.html', context=context)



# def about_me(request):
#     if request.method == 'GET':
#         return HttpResponse('Мое имя Жылдыз и я студентка GEEKS, по направлению Backend.')
    
# def current_time(request):
#     if request.method == 'GET':
#         time_now = dt.now()
#         hour = time_now.hour
#         time_str = time_now.strftime("%H:%M")
#         if 5<= hour <= 12:
#             period = f'{time_str} - Сейчас утро!'
#         elif 12< hour <= 14:
#             period = f'{time_str} - Сейчас обед!'
#         elif 14< hour <= 20:
#             period = f'{time_str} - Сейчас вечер!'
#         else:
#             period = f'{time_str} - НОЧЬ!'
#         return HttpResponse(period)


# def phrases_random_list(request):
#     if request.method == 'GET':
#         phrases_random = ['«Тяжелее всего человеку быть человеком изо дня в день» \n Ч. Айтматов', '«Неосмысленная жизнь не стоит того, чтобы жить» \n Сократ', '"Если вы не можете объяснить что-то шестилетнему ребенку, значит, вы сами этого не понимаете" \n Эйнштейн']
#         return HttpResponse(random.choice(phrases_random))
    