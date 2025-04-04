from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.decorators import login_required# add these 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView

from .models import Recipe, Comment
from .forms import MealForm


class Home(LoginView):
    template_name = 'home.html'

def about(request):
  
    return render(request, 'about.html')

@login_required
def recipe_index(request):
    recipes = Recipe.objects.filter(user=request.user)
    return render(request, 'recipes/index.html', {'recipes': recipes})

@login_required
def recipe_detail(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    meal_form = MealForm()
    return render(request, 'recipes/detail.html', {
        'recipe': recipe, 'meal_form': meal_form
    })

class RecipeCreate(LoginRequiredMixin, CreateView):
    model = Recipe
    fields = ['title', 'description', 'ingredients', 'instructions']
    def form_valid(self, form):
        form.instance.user = self.request.user  
        return super().form_valid(form)


class RecipeUpdate(LoginRequiredMixin, UpdateView):
    model = Recipe
    # Let's disallow the renaming of a cat by excluding the name field!
    fields = ['Title', 'description', 'ingredients']

class RecipeDelete(LoginRequiredMixin, DeleteView):
    model = Recipe
    success_url = '/recipes/'

@login_required
def add_meal(request, recipe_id):
    form = MealForm(request.POST)
    if form.is_valid():
        new_meal = form.save(commit=False)
        new_meal.recipe_id = recipe_id
        new_meal.save()
    return redirect('recipe-detail', recipe_id=recipe_id)

class CommentCreate(LoginRequiredMixin, CreateView):
    model = Comment
    fields = '__all__'

class CommentList(LoginRequiredMixin, ListView):
    model = Comment

class CommentDetail(√, DetailView):
    model = Comment

class CommentUpdate(LoginRequiredMixin, UpdateView):
    model = Comment
    fields = ['name', 'color']

class CommentDelete(LoginRequiredMixin, DeleteView):
    model = Comment
    success_url = '/comments/'

def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in
            login(request, user)
            return redirect('recipe-index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)
    # Same as: 
    # return render(
    #     request, 
    #     'signup.html',
    #     {'form': form, 'error_message': error_message}
    # )
