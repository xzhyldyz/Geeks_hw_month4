from django.db import models
from django.contrib.auth.models import User


class CustomUser(User):
    GENDER = (
        ('male','male'),
        ('female','female'),
        ('unknown','unknown')
    )
    POSITIONS = (
        ('Backend','Backend'),
        ('Frontend','Frontend'),
        ('Project Managment','Project Managment'),
        ('1C','1C'),
        ('UX/UI','UX/UI'),
        ('Тестировщик','Тестировщик')
    )
    phone_number = models.CharField(max_length=13, default="+996")
    gender = models.CharField(max_length=100, choices=GENDER, default='unknown')
    created_at = models.DateTimeField(auto_now_add=True)
    position = models.CharField(max_length=100, choices=POSITIONS, null=True)
    experience_years = models.CharField(max_length=2, default=0)

    def __str__(self):
        return self.username
    
     