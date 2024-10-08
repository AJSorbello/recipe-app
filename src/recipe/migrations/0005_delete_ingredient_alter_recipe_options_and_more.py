# Generated by Django 5.1 on 2024-08-29 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0004_ingredient'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Ingredient',
        ),
        migrations.AlterModelOptions(
            name='recipe',
            options={'ordering': ['name'], 'verbose_name': 'Recipe', 'verbose_name_plural': 'Recipes'},
        ),
        migrations.AlterField(
            model_name='recipe',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.TextField(default='Default description'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='difficulty',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='recipes/'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
