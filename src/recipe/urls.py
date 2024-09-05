from django.urls import path
from .views import (
    home,
    RecipeDetailView,
    RecipeListView,
)

app_name = "recipe"

urlpatterns = [
    path("", home, name="home"),
    path("recipe_list/", RecipeListView.as_view(), name="recipe_list"),
    path("recipe_list/<int:pk>/", RecipeDetailView.as_view(), name="recipe_detail"),
]