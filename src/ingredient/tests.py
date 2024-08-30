from django.test import TestCase
from decimal import Decimal
from recipe.models import Recipe  # Import Recipe model
from .models import Ingredient  # Import Ingredient model


class IngredientTestCase(TestCase):
    def setUp(self):
        # Setting up a sample Recipe and Ingredient for testing
        self.recipe = Recipe.objects.create(
            name="Spaghetti Bolognese",
            cooking_time=45,
            difficulty="Medium",
            description="A classic Italian dish.",
            instructions="Cook pasta and add sauce.",
        )
        self.ingredient = Ingredient.objects.create(
            recipe=self.recipe,
            name="Spaghetti",
            quantity=Decimal("200.0"),
            unit="grams",
        )

    def test_ingredient_creation(self):
        # Test that the ingredient is created successfully
        self.assertEqual(self.ingredient.name, "Spaghetti")
        self.assertEqual(self.ingredient.quantity, Decimal("200.0"))
        self.assertEqual(self.ingredient.unit, "grams")
        self.assertEqual(self.ingredient.recipe, self.recipe)

    def test_ingredient_string_representation(self):
        # Test the string representation of the ingredient
        expected_string = "200.0 grams of Spaghetti for Spaghetti Bolognese"
        self.assertEqual(str(self.ingredient), expected_string)
