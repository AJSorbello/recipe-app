from django.test import TestCase
from .models import Recipe

class RecipeModelTest(TestCase):
    def setUp(self):
        self.recipe = Recipe.objects.create(
            name="Test Recipe",
            description="Test Description",
            instructions="Test Instructions",
            cooking_time=45,
            difficulty="Medium"  # This will be recalculated in the save method
        )

    def test_recipe_creation(self):
        self.assertEqual(self.recipe.name, "Test Recipe")
        self.assertEqual(self.recipe.description, "Test Description")
        self.assertEqual(self.recipe.instructions, "Test Instructions")
        self.assertEqual(self.recipe.cooking_time, 45)
        # The difficulty should be recalculated based on cooking_time
        self.assertEqual(self.recipe.difficulty, "Medium")

    def test_calculate_difficulty_easy(self):
        self.recipe.cooking_time = 20
        self.recipe.save()
        self.assertEqual(self.recipe.difficulty, "Easy")

    def test_calculate_difficulty_medium(self):
        self.recipe.cooking_time = 45
        self.recipe.save()
        self.assertEqual(self.recipe.difficulty, "Medium")

    def test_calculate_difficulty_hard(self):
        self.recipe.cooking_time = 90
        self.recipe.save()
        self.assertEqual(self.recipe.difficulty, "Hard")

    def test_recipe_str(self):
        self.assertEqual(str(self.recipe), "Test Recipe")