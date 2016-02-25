from random import randint, choice
from .models import *
import time

MAX_NUMB_OF_INITIAL_MEAL_PLAN_GENERATED = 1000000

def get_meals(label):
  meals = []
  labels = MealLabel.objects.filter(label=label)


  for label in labels:
    servings = label.recipe.servings
    meal_info = [
      label.recipe.id,
      label.recipe.cost / servings,
      label.recipe.calories / servings,
      label.recipe.fat / servings,
      label.recipe.carbohydrates / servings,
      label.recipe.protein / servings,
      label.recipe.sat_fat / servings,
      label.recipe.trans_fat / servings,
      label.recipe.mono_unsat_fat / servings,
      label.recipe.poly_unsat_fat / servings,
      label.recipe.fiber / servings,
      label.recipe.sugar / servings,
      label.recipe.cholesterol / servings,
      label.recipe.sodium / servings,
      label.recipe.calcium / servings,
      label.recipe.magnesium / servings,
      label.recipe.potassium / servings,
      label.recipe.iron / servings,
      label.recipe.zinc / servings,
      label.recipe.phosphorus / servings,
      label.recipe.vit_a / servings,
      label.recipe.vit_c / servings,
      label.recipe.thiamin / servings,
      label.recipe.riboflavin / servings,
      label.recipe.niacin / servings,
      label.recipe.vit_b6 / servings,
      label.recipe.folic_acid / servings,
      label.recipe.vit_b12 / servings,
      label.recipe.vit_d / servings,
      label.recipe.vit_e / servings,
      label.recipe.vit_k / servings
    ]
    meals.append(meal_info)


  return meals

def generate_plan_meeting_nutrition(meals, nutrition_req):
  tries = 0
  while True:
    selected_meals = []
    tries += 1

    for i, meal in enumerate(meals):
      selected_meals.append(choice(meals[i]))

    met_nutrient_requirement = nutrition_met(selected_meals, nutrition_req)
    if met_nutrient_requirement:
      break

    if tries == MAX_NUMB_OF_INITIAL_MEAL_PLAN_GENERATED:
      break

  return selected_meals

def nutrition_met(meals, nutrition_req):
  nutrition_met = []
  meals_nutrition = get_nutrition(meals)

  for nutrition in nutrition_req:
    if nutrition in meals_nutrition:
      if meals_nutrition[nutrition] >= nutrition_req[nutrition]:
        nutrition_met.append(nutrition)

  if len(nutrition_met) >= (len(nutrition_req)):
    return True
  else:
    return False



def get_nutrition(meals):
    meals_nutrition = {
      'calories': 0,
      'fat': 0,
      'sat_fat': 0,
      'trans_fat': 0,
      'mono_unsat_fat': 0,
      'poly_unsat_fat': 0,
      'carbohydrates': 0,
      'fiber': 0,
      'sugar': 0,
      'protein': 0,
      'cholesterol': 0,
      'sodium': 0,
      'calcium': 0,
      'magnesium': 0,
      'potassium': 0,
      'iron': 0,
      'zinc': 0,
      'phosphorus': 0,
      'vit_a': 0,
      'vit_c': 0,
      'thiamin': 0,
      'riboflavin': 0,
      'niacin': 0,
      'vit_b6': 0,
      'folic_acid': 0,
      'vit_b12': 0,
      'vit_d': 0,
      'vit_e': 0,
      'vit_k': 0
    }

    for meal in meals:
      recipe = Recipe.objects.get(id=meal[0])
      meals_nutrition['calories'] += recipe.calories / recipe.servings
      meals_nutrition['fat'] += recipe.fat / recipe.servings
      meals_nutrition['sat_fat'] += recipe.sat_fat / recipe.servings
      meals_nutrition['trans_fat'] += recipe.trans_fat / recipe.servings
      meals_nutrition['mono_unsat_fat'] += recipe.mono_unsat_fat / recipe.servings
      meals_nutrition['poly_unsat_fat'] += recipe.poly_unsat_fat / recipe.servings
      meals_nutrition['carbohydrates'] += recipe.carbohydrates / recipe.servings
      meals_nutrition['fiber'] += recipe.fiber / recipe.servings
      meals_nutrition['sugar'] += recipe.sugar / recipe.servings
      meals_nutrition['protein'] += recipe.protein / recipe.servings
      meals_nutrition['cholesterol'] += recipe.cholesterol / recipe.servings
      meals_nutrition['sodium'] += recipe.sodium / recipe.servings
      meals_nutrition['calcium'] += recipe.calcium / recipe.servings
      meals_nutrition['magnesium'] += recipe.magnesium / recipe.servings
      meals_nutrition['potassium'] += recipe.potassium / recipe.servings
      meals_nutrition['iron'] += recipe.iron / recipe.servings
      meals_nutrition['zinc'] += recipe.zinc / recipe.servings
      meals_nutrition['phosphorus'] += recipe.phosphorus / recipe.servings
      meals_nutrition['vit_a'] += recipe.vit_a / recipe.servings
      meals_nutrition['vit_c'] += recipe.vit_c / recipe.servings
      meals_nutrition['thiamin'] += recipe.thiamin / recipe.servings
      meals_nutrition['riboflavin'] += recipe.riboflavin / recipe.servings
      meals_nutrition['niacin'] += recipe.niacin / recipe.servings
      meals_nutrition['vit_b6'] += recipe.vit_b6 / recipe.servings
      meals_nutrition['folic_acid'] += recipe.folic_acid / recipe.servings
      meals_nutrition['vit_b12'] += recipe.vit_b12 / recipe.servings
      meals_nutrition['vit_d'] += recipe.vit_d / recipe.servings
      meals_nutrition['vit_e'] += recipe.vit_e / recipe.servings
      meals_nutrition['vit_k'] += recipe.vit_k / recipe.servings      

    return meals_nutrition