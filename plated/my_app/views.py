from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Recipe


def home(request):
  
    return render(request, 'home.html')

def about(request):
  
    return render(request, 'about.html')

def recipe_index(request):
    recipes = Recipe.objects.all() 
    return render(request, 'recipes/index.html', {'recipes': recipes})

def recipe_detail(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    return render(request, 'recipes/detail.html', {'recipe': recipe})

class RecipeCreate(CreateView):
    model = Recipe
    fields = '__all__'

class RecipeUpdate(UpdateView):
    model = Recipe
    # Let's disallow the renaming of a cat by excluding the name field!
    fields = ['Title', 'description', 'ingredients']

class RecipeDelete(DeleteView):
    model = Recipe
    success_url = '/recipes/'