from django.db import models
from datetime import timedelta
from django.conf import settings

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    picture = models.URLField(blank=True)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    duration = models.DurationField(default=timedelta)
    rating = models.SmallIntegerField(default=0)



    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="recipes",
        on_delete=models.CASCADE,
        null=True,
    )


    def __str__(self):
        return self.title
# Create your models here.

class RecipeStep(models.Model):

    order = models.PositiveSmallIntegerField()
    instruction = models.TextField()
    recipe = models.ForeignKey(
        Recipe,
        related_name="steps",
        on_delete=models.CASCADE,
    )
    def recipe_title(self):
        return self.recipe.title

    class Meta:
        ordering = ["order"]

class Ingredient(models.Model):
    amount = models.CharField(max_length=100)
    food_item = models.CharField(max_length=100)

    recipe = models.ForeignKey(
        Recipe,
        related_name = "ingredients",
        on_delete=models.CASCADE,
    )
    class Meta:
        ordering = ["food_item"]