from django.db import models

class Recipe(models.Model):
    DIFFICULTY_CHOICES = [
        ("Easy", "Easy"),
        ("Medium", "Medium"),
        ("Hard", "Hard"),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    instructions = models.TextField()
    cooking_time = models.IntegerField()
    difficulty = models.CharField(max_length=50, choices=DIFFICULTY_CHOICES)
    
    image = models.ImageField(upload_to='recipe_list/images/', null=True, blank=True)

    def calculate_difficulty(self):
        if self.cooking_time < 30:
            self.difficulty = "Easy"
        elif 30 <= self.cooking_time <= 60:
            self.difficulty = "Medium"
        else:
            self.difficulty = "Hard"

    def save(self, *args, **kwargs):
        self.calculate_difficulty()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name