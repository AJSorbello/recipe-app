from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
from .models import Recipe

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "recipe/recipe_detail.html"  # Update the template name
    context_object_name = "recipe"

class RecipeListView(ListView):
    model = Recipe
    template_name = "recipe/recipe_list.html"
    context_object_name = "recipes"

def home(request):
    recipes = Recipe.objects.all()  # Fetch all recipes
    return render(request, "recipe/home.html", {"recipes": recipes})

def recipe_list(request):
    recipes = Recipe.objects.all()  # Add the namespace here
    return render(request, "recipes.html", {"recipes": recipes})

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, "recipe/recipe_detail.html", {"recipe": recipe})