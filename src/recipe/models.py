from django.db import models

class Recipe(models.Model):
    DIFFICULTY_CHOICES = [
        ("Easy", "Easy"),
        ("Medium", "Medium"),
        ("Hard", "Hard"),
    ]

    name = models.CharField(max_length=120)
    cooking_time = models.IntegerField(help_text="Cooking time in minutes")
    difficulty = models.CharField(max_length=50, choices=DIFFICULTY_CHOICES)
    description = models.TextField()
    instructions = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="recipe_list/images/", null=True, blank=True)  # Image field

    def __str__(self):
        return str(self.name)  # Ensure it returns a string

    def calculate_difficulty(self):
        if self.cooking_time < 30:
            self.difficulty = "Easy"
        elif self.cooking_time < 60:
            self.difficulty = "Medium"
        else:
            self.difficulty = "Hard"
        self.save()