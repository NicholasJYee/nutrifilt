from random import randint, choice
from .models import *
import time

MAX_NUMB_OF_INITIAL_MEAL_PLAN_GENERATED = 1000000

def get_meals(label):
  meals = []
  labels = MealLabel.objects.filter(label=label)


  for label in labels:
    start = time.time()
    cost = 0

    for ingredientrecipe in label.recipe.ingredientrecipe_set.all():
      ingredient_price = ingredientrecipe.ingredient.ingredientvendor_set.first().price
      weight_used = ingredientrecipe.weight
      ingredient_weight = ingredientrecipe.ingredient.ingredientvendor_set.first().weight
      cost += ingredient_price * weight_used / ingredient_weight
      cost = float("{0:.2f}".format(cost))
    end_cost = time.time()
    print(label.recipe, "inner loop time: ", end_cost - start)
    servings = label.recipe.servings
    meal_info = [
      label.id,
      cost,
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
    end = time.time()
    print("outer loop time: ", end - start)


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
      meals_nutrition['calories'] += meal.calories / meal.servings
      meals_nutrition['fat'] += meal.fat / meal.servings
      meals_nutrition['sat_fat'] += meal.sat_fat / meal.servings
      meals_nutrition['trans_fat'] += meal.trans_fat / meal.servings
      meals_nutrition['mono_unsat_fat'] += meal.mono_unsat_fat / meal.servings
      meals_nutrition['poly_unsat_fat'] += meal.poly_unsat_fat / meal.servings
      meals_nutrition['carbohydrates'] += meal.carbohydrates / meal.servings
      meals_nutrition['fiber'] += meal.fiber / meal.servings
      meals_nutrition['sugar'] += meal.sugar / meal.servings
      meals_nutrition['protein'] += meal.protein / meal.servings
      meals_nutrition['cholesterol'] += meal.cholesterol / meal.servings
      meals_nutrition['sodium'] += meal.sodium / meal.servings
      meals_nutrition['calcium'] += meal.calcium / meal.servings
      meals_nutrition['magnesium'] += meal.magnesium / meal.servings
      meals_nutrition['potassium'] += meal.potassium / meal.servings
      meals_nutrition['iron'] += meal.iron / meal.servings
      meals_nutrition['zinc'] += meal.zinc / meal.servings
      meals_nutrition['phosphorus'] += meal.phosphorus / meal.servings
      meals_nutrition['vit_a'] += meal.vit_a / meal.servings
      meals_nutrition['vit_c'] += meal.vit_c / meal.servings
      meals_nutrition['thiamin'] += meal.thiamin / meal.servings
      meals_nutrition['riboflavin'] += meal.riboflavin / meal.servings
      meals_nutrition['niacin'] += meal.niacin / meal.servings
      meals_nutrition['vit_b6'] += meal.vit_b6 / meal.servings
      meals_nutrition['folic_acid'] += meal.folic_acid / meal.servings
      meals_nutrition['vit_b12'] += meal.vit_b12 / meal.servings
      meals_nutrition['vit_d'] += meal.vit_d / meal.servings
      meals_nutrition['vit_e'] += meal.vit_e / meal.servings
      meals_nutrition['vit_k'] += meal.vit_k / meal.servings      

    return meals_nutrition