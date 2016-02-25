from random import randint, choice
from .models import *
import time

MAX_NUMB_OF_INITIAL_MEAL_PLAN_GENERATED = 500000

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
      label.recipe.sat_fat / servings,
      label.recipe.trans_fat / servings,
      label.recipe.mono_unsat_fat / servings,
      label.recipe.poly_unsat_fat / servings,
      label.recipe.carbohydrates / servings,
      label.recipe.fiber / servings,
      label.recipe.sugar / servings,
      label.recipe.protein / servings,
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

  for i, nutrition_req_amount in enumerate(nutrition_req):
    if meals_nutrition[i] >= nutrition_req_amount:
      nutrition_met.append(nutrition_req_amount)

  if len(nutrition_met) == (len(nutrition_req)):
    print meals_nutrition[0]
    return True
  else:
    return False



def get_nutrition(meals):
    meals_nutrition = [0] * 29

    for meal in meals:
      recipe = Recipe.objects.get(id=meal[0])
      meals_nutrition[0] += recipe.calories / recipe.servings
      meals_nutrition[1] += recipe.fat / recipe.servings
      meals_nutrition[2] += recipe.sat_fat / recipe.servings
      meals_nutrition[3] += recipe.trans_fat / recipe.servings
      meals_nutrition[4] += recipe.mono_unsat_fat / recipe.servings
      meals_nutrition[5] += recipe.poly_unsat_fat / recipe.servings
      meals_nutrition[6] += recipe.carbohydrates / recipe.servings
      meals_nutrition[7] += recipe.fiber / recipe.servings
      meals_nutrition[8] += recipe.sugar / recipe.servings
      meals_nutrition[9] += recipe.protein / recipe.servings
      meals_nutrition[10] += recipe.cholesterol / recipe.servings
      meals_nutrition[11] += recipe.sodium / recipe.servings
      meals_nutrition[12] += recipe.calcium / recipe.servings
      meals_nutrition[13] += recipe.magnesium / recipe.servings
      meals_nutrition[14] += recipe.potassium / recipe.servings
      meals_nutrition[15] += recipe.iron / recipe.servings
      meals_nutrition[16] += recipe.zinc / recipe.servings
      meals_nutrition[17] += recipe.phosphorus / recipe.servings
      meals_nutrition[18] += recipe.vit_a / recipe.servings
      meals_nutrition[19] += recipe.vit_c / recipe.servings
      meals_nutrition[20] += recipe.thiamin / recipe.servings
      meals_nutrition[21] += recipe.riboflavin / recipe.servings
      meals_nutrition[22] += recipe.niacin / recipe.servings
      meals_nutrition[23] += recipe.vit_b6 / recipe.servings
      meals_nutrition[24] += recipe.folic_acid / recipe.servings
      meals_nutrition[25] += recipe.vit_b12 / recipe.servings
      meals_nutrition[26] += recipe.vit_d / recipe.servings
      meals_nutrition[27] += recipe.vit_e / recipe.servings
      meals_nutrition[28] += recipe.vit_k / recipe.servings      

    return meals_nutrition