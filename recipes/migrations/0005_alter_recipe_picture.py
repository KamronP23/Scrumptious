# Generated by Django 4.1.3 on 2022-11-28 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0004_alter_recipe_rating"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="picture",
            field=models.URLField(blank=True),
        ),
    ]