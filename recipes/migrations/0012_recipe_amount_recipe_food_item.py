# Generated by Django 4.1.3 on 2022-12-01 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0011_recipe_instruction"),
    ]

    operations = [
        migrations.AddField(
            model_name="recipe",
            name="amount",
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AddField(
            model_name="recipe",
            name="food_item",
            field=models.CharField(default=0, max_length=100),
        ),
    ]