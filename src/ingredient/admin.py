from django.contrib import admin
from .models import Ingredient


class IngredientAdmin(admin.ModelAdmin):
    list_display = ("name", "quantity", "recipe")
    search_fields = ("name", "recipe__name")


admin.site.register(Ingredient, IngredientAdmin)
