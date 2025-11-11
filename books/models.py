from django.db import models
from django.conf import settings

class Book(models.Model):

    GENRE = (
        ('Роман','Роман'),
        ('Повесть','Повесть'),
        ('Рассказ','Рассказ'),
        ('Поэзия','Поэзия'),
        ('Драма','Драма'),
        ('Комедия','Комедия'),
        ('Трагедия','Трагедия')
    )
    title = models.CharField(max_length=100, verbose_name='ведите название книги')
    image = models.ImageField(upload_to='books/', verbose_name='загрузите обложку книги')
    annotation = models.TextField(verbose_name='ведите аннотацию книги')
    author = models.CharField(max_length=100, verbose_name='укажите автора', default='Автор неизвестен')
    genre = models.CharField(max_length=100, choices=GENRE, verbose_name='Укажите жанр')
    pages = models.PositiveIntegerField(verbose_name='укажите количество страницы', default=100)
    origin_language = models.CharField(max_length=100, verbose_name='укажите язык книги')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)


    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural ='Книги'


class Reviews(models.Model):

    MARK = (
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5')
    )
    choice_book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    mark = models.CharField(max_length=100, choices=MARK, default='4')
    comments = models.TextField()

    def __str__(self):
        return f'{self.choice_book} - {self.mark}'
    
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural ='Отзывы'