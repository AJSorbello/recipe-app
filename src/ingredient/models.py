from django.db import models
from recipe.models import Recipe  # Import the Recipe model


class Ingredient(models.Model):
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="ingredient_set"
    )
    name = models.CharField(max_length=255)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=50, blank=True, null=True, default="unit")

    def __str__(self):
        if self.unit:
            return f"{self.quantity} {self.unit} of {self.name} for {self.recipe.name}"
        return f"{self.quantity} of {self.name} for {self.recipe.name}"
