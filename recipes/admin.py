from django.contrib import admin
from recipes.models import Recipe, RecipeStep, Ingredient

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "duration",
        "rating",
        "id",
    )
 #Register your models here.
#admin.site.register(Recipe)

@admin.register(RecipeStep)
class RecipeStepAdmin(admin.ModelAdmin):
    list_display = (
        "order",
        "recipe_title",
        "id",
    )

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = (
        "amount",
        "food_item",
        "id",
    )


    