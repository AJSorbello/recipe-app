# Generated by Django 5.1.1 on 2024-09-12 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0010_remove_recipe_ingredients'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipe',
            options={},
        ),
        migrations.AlterField(
            model_name='recipe',
            name='name',
            field=models.CharField(max_length=120),
        ),
    ]
