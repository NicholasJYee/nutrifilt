from django.contrib import admin

# Register your models here.

from .models import Recipe, Ingredient, HealthLabel, IngredientRecipe
admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(HealthLabel)
admin.site.register(IngredientRecipe)