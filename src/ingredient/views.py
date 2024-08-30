from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from .models import Ingredient
from .forms import IngredientForm

class IngredientListView(ListView):
    model = Ingredient
    template_name = "ingredients/ingredient_list.html"
    context_object_name = "ingredients"

class IngredientDetailView(DetailView):
    model = Ingredient
    template_name = "ingredients/ingredient_detail.html"

def ingredient_create(request):
    if request.method == "POST":
        form = IngredientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("ingredients:ingredient-list")
    else:
        form = IngredientForm()
    return render(request, "ingredients/ingredient_form.html", {"form": form})

def ingredient_update(request, pk):
    ingredient = get_object_or_404(Ingredient, pk=pk)
    if request.method == "POST":
        form = IngredientForm(request.POST, instance=ingredient)
        if form.is_valid():
            form.save()
            return redirect("ingredients:ingredient-detail", pk=pk)
    else:
        form = IngredientForm(instance=ingredient)
    return render(request, "ingredients/ingredient_form.html", {"form": form})

def ingredient_delete(request, pk):
    ingredient = get_object_or_404(Ingredient, pk=pk)
    if request.method == "POST":
        ingredient.delete()
        return redirect("ingredients:ingredient-list")
    return render(request, "ingredients/ingredient_confirm_delete.html", {"ingredient": ingredient})from django.shortcuts import render

# Create your views here.
