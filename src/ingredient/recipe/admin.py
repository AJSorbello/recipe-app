from django.contrib import admin
from .models import Recipe


class RecipeAdmin(admin.ModelAdmin):
    """
    Admin view for the Recipe model.
    """

    list_display = ("name", "cooking_time", "difficulty")
    search_fields = ("name", "difficulty")


admin.site.register(Recipe, RecipeAdmin)
