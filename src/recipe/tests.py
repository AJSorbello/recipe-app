from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Recipe


class RecipeTestCase(TestCase):
    def setUp(self):
        # Set up initial data for testing
        self.recipe = Recipe.objects.create(
            name="Spaghetti Bolognese", cooking_time=45, difficulty="Medium"
        )

    def test_recipe_creation(self):
        # Test that the recipe is created successfully
        self.assertEqual(self.recipe.name, "Spaghetti Bolognese")
        self.assertEqual(self.recipe.cooking_time, 45)
        self.assertEqual(self.recipe.difficulty, "Medium")

    def test_recipe_string_representation(self):
        # Test the string representation of the recipe
        self.assertEqual(str(self.recipe), "Spaghetti Bolognese")
