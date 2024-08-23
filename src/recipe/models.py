from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=255)
    cooking_time = models.IntegerField()  # Time in minutes
    difficulty = models.CharField(
        max_length=50,
        choices=[("Easy", "Easy"), ("Medium", "Medium"), ("Hard", "Hard")],
    )

    def __str__(self):
        return self.name
