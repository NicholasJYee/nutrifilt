from django.contrib import admin

# Register your models here.

from .models import *
admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(Vendor)
admin.site.register(Plan)
admin.site.register(HealthLabel)
admin.site.register(MealLabel)
admin.site.register(IngredientRecipe)
admin.site.register(IngredientVendor)
admin.site.register(PlanRecipe)