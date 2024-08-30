from django.test import TestCase
from recipe.models import Recipe


class RecipeTestCase(TestCase):
    def setUp(self):
        # Setting up a sample Recipe for testing
        self.recipe = Recipe.objects.create(
            name="Spaghetti Bolognese",
            cooking_time=45,
            difficulty="Medium",
            description="A classic Italian dish.",
            instructions="Cook pasta and add sauce.",
        )

    def test_recipe_creation(self):
        # Test that the recipe is created successfully
        self.assertEqual(self.recipe.name, "Spaghetti Bolognese")
        self.assertEqual(self.recipe.cooking_time, 45)
        self.assertEqual(self.recipe.difficulty, "Medium")
        self.assertEqual(self.recipe.description, "A classic Italian dish.")
        self.assertEqual(self.recipe.instructions, "Cook pasta and add sauce.")

    def test_recipe_string_representation(self):
        # Test the string representation of the recipe
        self.assertEqual(str(self.recipe), "Spaghetti Bolognese")
