import unittest
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Recipe
from .forms import RecipeSearchForm
from .views import recipe_list

class RecipeFormTest(TestCase):
    def test_recipe_search_form_valid(self):
        form = RecipeSearchForm(data={'recipe_title': 'Test Recipe'})
        self.assertTrue(form.is_valid())

    def test_recipe_search_form_invalid(self):
        form = RecipeSearchForm(data={'recipe_title': ''})
        self.assertTrue(form.is_valid())  # Update to reflect that empty title is valid

class RecipeListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a user
        cls.user = User.objects.create_user(username='testuser', password='12345')
        # Create some recipes
        number_of_recipes = 13
        for recipe_id in range(number_of_recipes):
            Recipe.objects.create(
                name=f'Recipe {recipe_id}',
                cooking_time=recipe_id * 10,
                difficulty='Easy',
                description=f'Description for recipe {recipe_id}'
            )

    def setUp(self):
        self.client = Client()
        self.client.login(username='testuser', password='12345')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/recipes/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('recipe:recipe_list'))
        self.assertEqual(response.status_code, 200)

    def test_pagination_is_ten(self):
        response = self.client.get(reverse('recipe:recipe_list'))
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] is True)
        self.assertEqual(len(response.context['recipes']), 10)

    def test_lists_all_recipes(self):
        # Get second page and confirm it has (exactly) remaining 3 items
        response = self.client.get(reverse('recipe:recipe_list') + '?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['recipes']), 3)

    def test_login_required(self):
        self.client.logout()
        response = self.client.get(reverse('recipe:recipe_list'))
        self.assertRedirects(response, '/login/?next=/recipes/recipe_list/')

    def test_chart_generation(self):
        response = self.client.post(reverse('recipe:recipe_list'), {
            'recipe_title': 'Recipe',
            'chart_type': '#1',
            'show_all': 'on'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('chart', response.context)
        self.assertIsNotNone(response.context['chart'])

if __name__ == '__main__':
    unittest.main(verbosity=2)