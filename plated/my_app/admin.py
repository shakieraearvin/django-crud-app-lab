from django.contrib import admin
from .models import Recipe, Meal, Comment

admin.site.register(Recipe)
admin.site.register(Meal)
admin.site.register(Comment)
# Register your models here.
