from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    
class Rating(models.Model):
    rat = models.CharField()

    def __str__(self):
        return self.rat  
    

class Film(models.Model):
    GENRE = (
        ('Фантастика', 'Фантастика'),
        ('Ужасы','Ужасы'),
        ('Мелодрамма','Мелодрамма'),
        ('Боевик','Боевик')
    )
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='films/', blank=True, null= True)
    description = models.TextField()
    genre = models.CharField(max_length=100, choices=GENRE)
    created_date = models.DateField(auto_now_add=True)
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE, null=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return str(self.title)
    
