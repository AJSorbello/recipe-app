from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Recipe
from .forms import RecipeSearchForm
import pandas as pd
from .utils import get_recipe_from_id, get_chart

def home(request):
    return render(request, "recipe/home.html")

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, "recipe/recipe_detail.html", {'recipe': recipe})

@login_required
def recipe_list(request):
    form = RecipeSearchForm(request.POST or None)
    recipe_df_html = None  # Initialize recipe_df_html
    chart = None
    recipes = Recipe.objects.all()  # Default to all recipes

    if request.method == 'POST':
        recipe_title = request.POST.get('recipe_title')
        chart_type = request.POST.get('chart_type')
        print(f"Search term: {recipe_title}, Chart type: {chart_type}")
        
        qs = Recipe.objects.filter(name__icontains=recipe_title)
        print(f"Filtered QuerySet: {qs}")

        if qs.exists():
            recipes = qs  # Update the recipes variable to use the filtered queryset
            recipe_df = pd.DataFrame(list(qs.values()))
            print(f"DataFrame: {recipe_df}")

            # Process DataFrame
            recipe_df['name'] = recipe_df['id'].apply(get_recipe_from_id)
            recipe_df_html = recipe_df.to_html(index=False, columns=['id', 'name', 'cooking_time', 'difficulty'])
            print(f"DataFrame HTML: {recipe_df_html}")

            # Generate chart
            chart = get_chart(chart_type, recipe_df, labels=recipe_df['name'].values)
            print(f"Generated Chart: {chart}")

    context = {
        'form': form,
        'recipes': recipes,
        'recipe_df': recipe_df_html,
        'chart': chart,
    }
    return render(request, "recipe/recipe_list.html", context)