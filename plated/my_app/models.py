from django.db import models
from django.urls import reverse

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    ingredients = models.TextField(max_length=250)
    instructions = models.TextField(max_length=250)

    def __str__(self):
         return f'{self.title} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('recipe-detail', kwargs={'recipe_id': self.id})