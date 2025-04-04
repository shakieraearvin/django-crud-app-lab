from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    ingredients = models.TextField(max_length=250)
    instructions = models.TextField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
         return f'{self.title} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('recipe-detail', kwargs={'recipe_id': self.id})
    


class Meal(models.Model):
    date = models.DateField('Date Made')
    type = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0]
    )

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_type_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']  

# Add the Toy model
class Comment(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField(max_length=250)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('comment-detail', kwargs={'pk': self.id})
