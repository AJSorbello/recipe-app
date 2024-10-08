# Generated by Django 5.1.1 on 2024-09-20 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipe", "0012_alter_recipe_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="cooking_time",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="recipe",
            name="instructions",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="recipe",
            name="name",
            field=models.CharField(max_length=255),
        ),
    ]
