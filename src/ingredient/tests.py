from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Ingredient
from recipe.models import Recipe  # Importing Recipe model for foreign key relation


class IngredientTestCase(TestCase):
    def setUp(self):
        # Set up initial data for testing
        self.recipe = Recipe.objects.create(
            name="Spaghetti Bolognese", cooking_time=45, difficulty="Medium"
        )
        self.ingredient = Ingredient.objects.create(
            recipe=self.recipe, name="Spaghetti", quantity="200g"
        )

    def test_ingredient_creation(self):
        # Test that the ingredient is created successfully
        self.assertEqual(self.ingredient.name, "Spaghetti")
        self.assertEqual(self.ingredient.quantity, "200g")
        self.assertEqual(self.ingredient.recipe, self.recipe)

    def test_ingredient_string_representation(self):
        # Test the string representation of the ingredient
        expected_string = "200g of Spaghetti for Spaghetti Bolognese"
        self.assertEqual(str(self.ingredient), expected_string)
