from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Recipe(models.Model):
  label = models.CharField(max_length=100)
  image = models.CharField(max_length=512)
  url = models.CharField(max_length=512)
  servings = models.FloatField()
  calories = models.FloatField()
  fat = models.FloatField()
  sat_fat = models.FloatField()
  trans_fat = models.FloatField()
  mono_unsat_fat = models.FloatField()
  poly_unsat_fat = models.FloatField()
  carbohydrates = models.FloatField()
  fiber = models.FloatField()
  sugar = models.FloatField()
  protein = models.FloatField()
  cholesterol = models.FloatField()
  sodium = models.FloatField()
  calcium = models.FloatField()
  magnesium = models.FloatField()
  potassium = models.FloatField()
  iron = models.FloatField()
  zinc = models.FloatField()
  phosphorus = models.FloatField()
  vit_a = models.FloatField()
  vit_c = models.FloatField()
  thiamin = models.FloatField()
  riboflavin = models.FloatField()
  niacin = models.FloatField()
  vit_b6 = models.FloatField()
  folic_acid = models.FloatField()
  vit_b12 = models.FloatField()
  vit_d = models.FloatField()
  vit_e = models.FloatField()
  vit_k = models.FloatField()
  created_on = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.label

class Ingredient(models.Model):
  food = models.CharField(max_length=100)
  created_on = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.food

class Vendor(models.Model):
  name = models.CharField(max_length=100)
  created_on = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name

class Plan(models.Model):
  name = models.CharField(max_length=150)
  calories = models.FloatField()
  fat = models.FloatField()
  sat_fat = models.FloatField()
  trans_fat = models.FloatField()
  mono_unsat_fat = models.FloatField()
  poly_unsat_fat = models.FloatField()
  carbohydrates = models.FloatField()
  fiber = models.FloatField()
  sugar = models.FloatField()
  protein = models.FloatField()
  cholesterol = models.FloatField()
  sodium = models.FloatField()
  calcium = models.FloatField()
  magnesium = models.FloatField()
  potassium = models.FloatField()
  iron = models.FloatField()
  zinc = models.FloatField()
  phosphorus = models.FloatField()
  vit_a = models.FloatField()
  vit_c = models.FloatField()
  thiamin = models.FloatField()
  riboflavin = models.FloatField()
  niacin = models.FloatField()
  vit_b6 = models.FloatField()
  folic_acid = models.FloatField()
  vit_b12 = models.FloatField()
  vit_d = models.FloatField()
  vit_e = models.FloatField()
  vit_k = models.FloatField()
  created_on = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name

class HealthLabel(models.Model):
  recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
  label = models.CharField(max_length=150)
  created_on = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now=True)

  def __str__(self):
    return str(self.recipe.label) + ":\t" + str(self.label)
    
class MealLabel(models.Model):
  recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
  label = models.CharField(max_length=150)
  created_on = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now=True)

  def __str__(self):
    return str(self.recipe.label) + ":\t" + str(self.label)

class IngredientRecipe(models.Model):
  recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
  ingredient = models.ForeignKey(Ingredient)
  text = models.CharField(max_length=150)
  food = models.CharField(max_length=100)
  weight = models.FloatField()
  created_on = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.text

class IngredientVendor(models.Model):
  vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
  ingredient = models.ForeignKey(Ingredient)
  product = models.CharField(max_length=200)
  weight = models.FloatField()
  price = models.FloatField()
  created_on = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.product  

class PlanRecipe(models.Model):
  plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
  recipe = models.ForeignKey(Recipe)
  meal_number = models.FloatField()
  created_on = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.plan.name + ":\t" + str(self.meal_number)