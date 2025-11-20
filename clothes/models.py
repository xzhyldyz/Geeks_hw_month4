from django.db import models


class CategoryClothes(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Products(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default='описание продукта')
    tags = models.ManyToManyField(CategoryClothes)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}-{", ".join(i.name for i in self.tags.all() )}'