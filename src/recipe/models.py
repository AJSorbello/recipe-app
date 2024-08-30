from django.db import models


class Recipe(models.Model):
    DIFFICULTY_CHOICES = [
        ("Easy", "Easy"),
        ("Medium", "Medium"),
        ("Hard", "Hard"),
    ]

    name = models.CharField(max_length=255)
    cooking_time = models.IntegerField(help_text="Cooking time in minutes")
    difficulty = models.CharField(max_length=50, choices=DIFFICULTY_CHOICES)
    description = models.TextField()
    instructions = models.TextField(null=True, blank=True)
    image = models.ImageField(
        upload_to="recipe_list/images/", null=True, blank=True
    )  # Image field

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "Recipe"
        verbose_name_plural = "Recipes"
