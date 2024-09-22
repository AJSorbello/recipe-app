from django.urls import path
from .views import (
    home,
    recipe_list,
    recipe_detail,
)

app_name = "recipe"

urlpatterns = [
    path("", home, name="home"),
    path("recipe_list/", recipe_list, name="recipe_list"),
    path("recipe_list/<int:pk>/", recipe_detail, name="recipe_detail"),
]
