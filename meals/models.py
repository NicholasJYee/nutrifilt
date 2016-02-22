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
  ingredient = models.ForeignKey(Ingredient, blank=True, null=True)
  text = models.CharField(max_length=150)
  food = models.CharField(max_length=100)
  weight = models.FloatField()
  created_on = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.recipe.label + ":\t" + self.text

class IngredientVendor(models.Model):
  vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
  ingredient = models.ForeignKey(Ingredient, blank=True, null=True)
  product = models.CharField(max_length=200)
  weight = models.FloatField()
  price = models.FloatField()
  created_on = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.vendor.name + ":\t" + self.product  

class PlanRecipe(models.Model):
  plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
  recipe = models.ForeignKey(Recipe)
  meal_number = models.FloatField()
  created_on = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.plan.name + ":\t" + str(self.meal_number)