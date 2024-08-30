from django.urls import path
from .views import (
    IngredientListView,
    IngredientDetailView,
    ingredient_create,
    ingredient_update,
    ingredient_delete,
)

app_name = "ingredients"

urlpatterns = [
    path("", IngredientListView.as_view(), name="ingredient-list"),
    path("<int:pk>/", IngredientDetailView.as_view(), name="ingredient-detail"),
    path("create/", ingredient_create, name="ingredient-create"),
    path("<int:pk>/update/", ingredient_update, name="ingredient-update"),
    path("<int:pk>/delete/", ingredient_delete, name="ingredient-delete"),
]
