from django.test import TestCase
from django.urls import reverse
from .models import Recipe

class RecipeListViewTest(TestCase):
    def setUp(self):
        # Create 20 recipes for testing
        for i in range(20):
            Recipe.objects.create(
                name=f"Test Recipe {i}",
                description="Test Description",
                instructions="Test Instructions",
                cooking_time=45,
                difficulty="Medium"
            )

    def test_recipe_list_view(self):
        response = self.client.get(reverse('recipe:recipe_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe/recipe_list.html')
        self.assertEqual(len(response.context['recipes']), 15)  # Check for 15 recipes on the first page
        self.assertTrue(response.context['is_paginated'])

    def test_recipe_list_view_second_page(self):
        response = self.client.get(reverse('recipe:recipe_list') + '?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe/recipe_list.html')
        self.assertEqual(len(response.context['recipes']), 5)  # Check for 5 recipes on the second page
        self.assertTrue(response.context['is_paginated'])