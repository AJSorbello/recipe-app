from django.db import models
from recipe.models import Recipe  # Importing Recipe model from its respective app


class Ingredient(models.Model):
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="ingredients"
    )
    name = models.CharField(max_length=255)
    quantity = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.quantity} of {self.name} for {self.recipe.name}"
