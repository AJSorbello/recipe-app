from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Recipe
from .forms import RecipeSearchForm
import pandas as pd
from .utils import get_recipe_from_id

def home(request):
    return render(request, "recipe/home.html")

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, "recipe/recipe_detail.html", {'recipe': recipe})

@login_required
def recipe_list(request):
    form = RecipeSearchForm(request.POST or None)
    recipe_df = None
    chart = None
    recipes = Recipe.objects.all()  # Default to all recipes

    if request.method == 'POST':
        recipe_title = request.POST.get('recipe_title')
        chart_type = request.POST.get('chart_type')
        print(recipe_title, chart_type)
        
        print('Exploring querysets:')
        print('Case 1: Output of Recipe.objects.all()')
        qs = Recipe.objects.all()
        print(qs)

        print('Case 2: Output of Recipe.objects.filter(name__icontains=recipe_title)')
        qs = Recipe.objects.filter(name__icontains=recipe_title)
        print(qs)

        print('Case 3: Output of qs.values()')
        print(qs.values())

        print('Case 4: Output of qs.values_list()')
        print(qs.values_list())

        print('Case 5: Output of Recipe.objects.get(id=1)')
        obj = Recipe.objects.get(id=1)
        print(obj)

        if qs.exists():
            recipes = qs  # Update the recipes variable to use the filtered queryset
            recipe_df = pd.DataFrame(qs.values())
            recipe_df['recipe_id'] = recipe_df['id'].apply(get_recipe_from_id)
            # chart = get_chart(chart_type, recipe_df, labels=recipe_df['recipe_id'].values)
            recipe_df = recipe_df.to_html()

    context = {
        'form': form,
        'recipes': recipes,
        'recipe_df': recipe_df,
        'chart': chart,
    }
    return render(request, "recipe/recipe_list.html", context)