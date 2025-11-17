from django.db import models
from books.models import *

class Order(models.Model):
    STATUS = (
        ('новый','новый'),
        ('обработан','обработан')
    )
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=1)

    name = models.CharField(max_length=100, verbose_name='Введите имя:')
    phone = models.CharField(max_length=20, verbose_name='Введите номер телефона:')
    address = models.CharField(max_length=255, verbose_name='Введите ваш адресс:')
    
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS, max_length=50)
