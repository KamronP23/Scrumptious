# Generated by Django 4.1.3 on 2022-11-23 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0002_recipe_duration_recipe_rating"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="rating",
            field=models.DecimalField(decimal_places=2, max_digits=2, null=True),
        ),
    ]
