from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Recipe(models.Model):
  label = models.CharField(max_length=100)
  image = models.CharField(max_length=512, blank=True, null=True)
  url = models.CharField(max_length=512, blank=True, null=True)
  servings = models.FloatField(blank=True, null=True)
  calories = models.FloatField(blank=True, null=True)
  fat = models.FloatField(blank=True, null=True)
  sat_fat = models.FloatField(blank=True, null=True)
  trans_fat = models.FloatField(blank=True, null=True)
  mono_unsat_fat = models.FloatField(blank=True, null=True)
  poly_unsat_fat = models.FloatField(blank=True, null=True)
  carbohydrates = models.FloatField(blank=True, null=True)
  fiber = models.FloatField(blank=True, null=True)
  sugar = models.FloatField(blank=True, null=True)
  protein = models.FloatField(blank=True, null=True)
  cholesterol = models.FloatField(blank=True, null=True)
  sodium = models.FloatField(blank=True, null=True)
  calcium = models.FloatField(blank=True, null=True)
  magnesium = models.FloatField(blank=True, null=True)
  potassium = models.FloatField(blank=True, null=True)
  iron = models.FloatField(blank=True, null=True)
  zinc = models.FloatField(blank=True, null=True)
  phosphorus = models.FloatField(blank=True, null=True)
  vit_a = models.FloatField(blank=True, null=True)
  vit_c = models.FloatField(blank=True, null=True)
  thiamin = models.FloatField(blank=True, null=True)
  riboflavin = models.FloatField(blank=True, null=True)
  niacin = models.FloatField(blank=True, null=True)
  vit_b6 = models.FloatField(blank=True, null=True)
  folic_acid = models.FloatField(blank=True, null=True)
  vit_b12 = models.FloatField(blank=True, null=True)
  vit_d = models.FloatField(blank=True, null=True)
  vit_e = models.FloatField(blank=True, null=True)
  vit_k = models.FloatField(blank=True, null=True)
  created_on = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.label.encode('utf-8')

class Ingredient(models.Model):
  food = models.CharField(max_length=100)
  created_on = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.food.encode('utf-8')

class Vendor(models.Model):
  name = models.CharField(max_length=100)
  created_on = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name.encode('utf-8')

class Plan(models.Model):
  name = models.CharField(max_length=150)
  calories = models.FloatField(blank=True, null=True)
  fat = models.FloatField(blank=True, null=True)
  sat_fat = models.FloatField(blank=True, null=True)
  trans_fat = models.FloatField(blank=True, null=True)
  mono_unsat_fat = models.FloatField(blank=True, null=True)
  poly_unsat_fat = models.FloatField(blank=True, null=True)
  carbohydrates = models.FloatField(blank=True, null=True)
  fiber = models.FloatField(blank=True, null=True)
  sugar = models.FloatField(blank=True, null=True)
  protein = models.FloatField(blank=True, null=True)
  cholesterol = models.FloatField(blank=True, null=True)
  sodium = models.FloatField(blank=True, null=True)
  calcium = models.FloatField(blank=True, null=True)
  magnesium = models.FloatField(blank=True, null=True)
  potassium = models.FloatField(blank=True, null=True)
  iron = models.FloatField(blank=True, null=True)
  zinc = models.FloatField(blank=True, null=True)
  phosphorus = models.FloatField(blank=True, null=True)
  vit_a = models.FloatField(blank=True, null=True)
  vit_c = models.FloatField(blank=True, null=True)
  thiamin = models.FloatField(blank=True, null=True)
  riboflavin = models.FloatField(blank=True, null=True)
  niacin = models.FloatField(blank=True, null=True)
  vit_b6 = models.FloatField(blank=True, null=True)
  folic_acid = models.FloatField(blank=True, null=True)
  vit_b12 = models.FloatField(blank=True, null=True)
  vit_d = models.FloatField(blank=True, null=True)
  vit_e = models.FloatField(blank=True, null=True)
  vit_k = models.FloatField(blank=True, null=True)
  created_on = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name.encode('utf-8')

  def cost(self):
    cost = 0
    for meal in self.planrecipe_set.all():
      for ingredientrecipe in meal.recipe.ingredientrecipe_set.all():
        ingredient_price = ingredientrecipe.ingredient.ingredientvendor_set.first().price
        weight_used = ingredientrecipe.weight
        ingredient_weight = ingredientrecipe.ingredient.ingredientvendor_set.first().weight
        cost += ingredient_price * weight_used / ingredient_weight
    return round(cost, 2)

class HealthLabel(models.Model):
  recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
  label = models.CharField(max_length=150)
  created_on = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.recipe.label.encode('utf-8') + ":\t" + self.label.encode('utf-8')
    
class MealLabel(models.Model):
  recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
  label = models.CharField(max_length=150)
  created_on = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.recipe.label.encode('utf-8') + ":\t" + self.label.encode('utf-8')

class IngredientRecipe(models.Model):
  recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
  ingredient = models.ForeignKey(Ingredient, blank=True, null=True)
  text = models.CharField(max_length=300)
  food = models.CharField(max_length=100)
  weight = models.FloatField()
  created_on = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.recipe.label.encode('utf-8') + ":\t" + self.food.encode('utf-8')

class IngredientVendor(models.Model):
  vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
  ingredient = models.ForeignKey(Ingredient, blank=True, null=True)
  product = models.CharField(max_length=200)
  weight = models.FloatField()
  price = models.FloatField()
  created_on = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.vendor.name.encode('utf-8') + ":\t" + self.product.encode('utf-8') 

class PlanRecipe(models.Model):
  plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
  recipe = models.ForeignKey(Recipe)
  meal_number = models.FloatField()
  created_on = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.plan.name.encode('utf-8') + ":\t" + str(self.meal_number)