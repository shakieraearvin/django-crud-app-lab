from django.shortcuts import render

# Create your views here.

# Import HttpResponse to send text-based responses
from django.http import HttpResponse



class Recipe:
    def __init__(self, title, description, ingredients, instructions):
        self.title = title
        self.description = description
        self.ingredients = ingredients
        self.instructions = instructions

# Create a list of Cat instances
recipes = [
    Recipe("Lemon Garlic Salmon", "A light and flavorful salmon dish with lemon and garlic.", "Salmon fillet, lemon juice, garlic, olive oil, salt, pepper", "1. Preheat oven to 375°F. 2. Mix lemon juice, garlic, and olive oil. 3. Pour over salmon. 4. Bake for 15-20 minutes."),

    Recipe("Spaghetti Aglio e Olio", "Simple and delicious pasta with garlic and olive oil.", "Spaghetti, garlic, olive oil, red pepper flakes, parsley, salt", "1. Cook pasta. 2. Sauté garlic in olive oil. 3. Add red pepper flakes. 4. Toss with pasta and parsley."),

    Recipe("Avocado Toast", "Classic avocado toast with optional toppings.", "Bread, avocado, salt, pepper, lemon juice, red pepper flakes", "1. Toast bread. 2. Mash avocado with lemon juice, salt, and pepper. 3. Spread on toast. 4. Add toppings as desired."),

    Recipe("Avocado Toast", "Classic avocado toast with optional toppings.", "Bread, avocado, salt, pepper, lemon juice, red pepper flakes", "1. Toast bread. 2. Mash avocado with lemon juice, salt, and pepper. 3. Spread on toast. 4. Add toppings as desired.")
]

def recipe_index(request):
    # Render the cats/index.html template with the cats data
    return render(request, 'recipes/index.html', {'recipes': recipes})

def home(request):
  
    return render(request, 'home.html')

def about(request):
  
    return render('request, about.html')

