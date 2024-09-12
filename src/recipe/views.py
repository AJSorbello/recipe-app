from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
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
    chart_type = None  # Initialize chart_type

    # Fetch all recipes for the chart
    all_recipes = Recipe.objects.all()
    all_recipe_df = pd.DataFrame(list(all_recipes.values()))
    all_recipe_df['name'] = all_recipe_df['id'].apply(get_recipe_from_id)

    if request.method == 'POST':
        recipe_title = request.POST.get('recipe_title')
        chart_type = request.POST.get('chart_type')
        show_all = request.POST.get('show_all')
        print(f"Search term: {recipe_title}, Chart type: {chart_type}, Show All: {show_all}")
        
        if show_all:
            recipes = Recipe.objects.all()
            recipe_df = pd.DataFrame(list(recipes.values()))
            recipe_df['name'] = recipe_df['id'].apply(get_recipe_from_id)
            recipe_df_html = recipe_df.to_html(index=False, columns=['id', 'name', 'cooking_time', 'difficulty'])
        else:
            qs = Recipe.objects.filter(name__icontains=recipe_title)
            print(f"Filtered QuerySet: {qs}")

            if qs.exists():
                recipes = qs  # Update the recipes variable to use the filtered queryset
                recipe_df = pd.DataFrame(list(qs.values()))
                print(f"DataFrame: {recipe_df[['id', 'name', 'cooking_time', 'difficulty']]}")

                # Process DataFrame
                recipe_df['name'] = recipe_df['id'].apply(get_recipe_from_id)
                recipe_df_html = recipe_df.to_html(index=False, columns=['id', 'name', 'cooking_time', 'difficulty'])
            else:
                recipe_df = pd.DataFrame()  # Empty DataFrame if no results

    # Generate chart based on the filtered or all recipes
    if chart_type:
        if show_all:
            chart = get_chart(chart_type, all_recipe_df, labels=all_recipe_df['name'].tolist(), cooking_times=all_recipe_df['cooking_time'].tolist())
        else:
            if not recipe_df.empty:
                chart = get_chart(chart_type, recipe_df, labels=recipe_df['name'].tolist(), cooking_times=recipe_df['cooking_time'].tolist())
            else:
                chart = get_chart(chart_type, all_recipe_df, labels=all_recipe_df['name'].tolist(), cooking_times=all_recipe_df['cooking_time'].tolist())
        print(f"Generated Chart: {chart[:100]}...")  # Print only the first 100 characters of the chart

    # Pagination
    paginator = Paginator(recipes, 10)  # Show 10 recipes per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'form': form,
        'recipes': page_obj,  # Use the paginated recipes
        'recipe_df': recipe_df_html,
        'chart': chart,
        'is_paginated': page_obj.has_other_pages(),  # Add pagination info to context
    }
    return render(request, "recipe/recipe_list.html", context)