from random import randint, choice
from .models import *
import time
from numpy import vstack, array

MAX_NUMB_OF_INITIAL_MEAL_PLAN_GENERATED = 500000

def get_nutrition_req(form):
  nutrition_req = []

  if form.cleaned_data['calories'] is not None:
    nutrition_req.append(form.cleaned_data['calories'])
  else:
    nutrition_req.append(0)
  if form.cleaned_data['fat'] is not None:
    nutrition_req.append(form.cleaned_data['fat'])
  else:
    nutrition_req.append(0)
  if form.cleaned_data['sat_fat'] is not None:
    nutrition_req.append(form.cleaned_data['sat_fat'])
  else:
    nutrition_req.append(0)
  if form.cleaned_data['trans_fat'] is not None:
    nutrition_req.append(form.cleaned_data['trans_fat'])
  else:
    nutrition_req.append(0)
  if form.cleaned_data['mono_unsat_fat'] is not None:
    nutrition_req.append(form.cleaned_data['mono_unsat_fat'])
  else:
    nutrition_req.append(0)
  if form.cleaned_data['poly_unsat_fat'] is not None:
    nutrition_req.append(form.cleaned_data['poly_unsat_fat'])
  else:
    nutrition_req.append(0)
  if form.cleaned_data['carbohydrates'] is not None:
    nutrition_req.append(form.cleaned_data['carbohydrates'])
  else:
    nutrition_req.append(0)
  if form.cleaned_data['fiber'] is not None:
    nutrition_req.append(form.cleaned_data['fiber'])
  else:
    nutrition_req.append(0)
  if form.cleaned_data['sugar'] is not None:
    nutrition_req.append(form.cleaned_data['sugar'])
  else:
    nutrition_req.append(0)
  if form.cleaned_data['protein'] is not None:
    nutrition_req.append(form.cleaned_data['protein'])
  else:
    nutrition_req.append(0)
  if form.cleaned_data['cholesterol'] is not None:
    nutrition_req.append(form.cleaned_data['cholesterol'])
  else:
    nutrition_req.append(0)
  if form.cleaned_data['sodium'] is not None:
    nutrition_req.append(form.cleaned_data['sodium'])
  else:
    nutrition_req.append(0)
  if form.cleaned_data['calcium'] is not None:
    nutrition_req.append(form.cleaned_data['calcium'])
  else:
    nutrition_req.append(0)
  if form.cleaned_data['magnesium'] is not None:
    nutrition_req.append(form.cleaned_data['magnesium'])
  else:
    nutrition_req.append(0)
  if form.cleaned_data['potassium'] is not None:
    nutrition_req.append(form.cleaned_data['potassium'])
  else:
    nutrition_req.append(0)
  if form.cleaned_data['iron'] is not None:
    nutrition_req.append(form.cleaned_data['iron'])
  else:
    nutrition_req.append(0)
  if form.cleaned_data['zinc'] is not None:
    nutrition_req.append(form.cleaned_data['zinc'])
  else:
    nutrition_req.append(0)
  if form.cleaned_data['phosphorus'] is not None:
    nutrition_req.append(form.cleaned_data['phosphorus'])
  else:
    nutrition_req.append(0)
  if form.cleaned_data['vit_a'] is not None:
    nutrition_req.append(form.cleaned_data['vit_a'] * 0.3)
  else:
    nutrition_req.append(0)
  if form.cleaned_data['vit_c'] is not None:
    nutrition_req.append(form.cleaned_data['vit_c'])
  else:
    nutrition_req.append(0)
  if form.cleaned_data['thiamin'] is not None:
    nutrition_req.append(form.cleaned_data['thiamin'])
  else:
    nutrition_req.append(0)
  if form.cleaned_data['riboflavin'] is not None:
    nutrition_req.append(form.cleaned_data['riboflavin'])
  else:
    nutrition_req.append(0)
  if form.cleaned_data['niacin'] is not None:
    nutrition_req.append(form.cleaned_data['niacin'])
  else:
    nutrition_req.append(0)
  if form.cleaned_data['vit_b6'] is not None:
    nutrition_req.append(form.cleaned_data['vit_b6'])
  else:
    nutrition_req.append(0)
  if form.cleaned_data['folic_acid'] is not None:
    nutrition_req.append(form.cleaned_data['folic_acid'])
  else:
    nutrition_req.append(0)
  if form.cleaned_data['vit_b12'] is not None:
    nutrition_req.append(form.cleaned_data['vit_b12'])
  else:
    nutrition_req.append(0)
  if form.cleaned_data['vit_d'] is not None:
    nutrition_req.append(form.cleaned_data['vit_d'] * 0.025)
  else:
    nutrition_req.append(0)
  if form.cleaned_data['vit_e'] is not None:
    nutrition_req.append(form.cleaned_data['vit_e'] * 0.9)
  else:
    nutrition_req.append(0)
  if form.cleaned_data['vit_k'] is not None:
    nutrition_req.append(form.cleaned_data['vit_k'])
  else:
    nutrition_req.append(0)

  return nutrition_req

def get_meals(label, health_labels):
  meals = []
  try:
    label0 = MealLabel.objects.filter(label=label, recipe__healthlabel__label=health_labels[0])
    try:
      label1 = MealLabel.objects.filter(label=label, recipe__healthlabel__label=health_labels[1])
      try:
        label2 = MealLabel.objects.filter(label=label, recipe__healthlabel__label=health_labels[2])
        try:
          label3 = MealLabel.objects.filter(label=label, recipe__healthlabel__label=health_labels[3])
          try:
            label4 = MealLabel.objects.filter(label=label, recipe__healthlabel__label=health_labels[4])
            try:
              label5 = MealLabel.objects.filter(label=label, recipe__healthlabel__label=health_labels[5])
              try:
                label6 = MealLabel.objects.filter(label=label, recipe__healthlabel__label=health_labels[6])
                try:
                  label7 = MealLabel.objects.filter(label=label, recipe__healthlabel__label=health_labels[7])
                  try:
                    label8 = MealLabel.objects.filter(label=label, recipe__healthlabel__label=health_labels[8])
                    try:
                      label9 = MealLabel.objects.filter(label=label, recipe__healthlabel__label=health_labels[9])
                      try:
                        label10 = MealLabel.objects.filter(label=label, recipe__healthlabel__label=health_labels[10])
                        try:
                          label11 = MealLabel.objects.filter(label=label, recipe__healthlabel__label=health_labels[11])
                          labels = set(label0).intersection(label1).intersection(label2).intersection(label3).intersection(label4).intersection(label5).intersection(label6).intersection(label7).intersection(label8).intersection(label9).intersection(label10).intersection(label11)
                        except IndexError:
                          labels = set(label0).intersection(label1).intersection(label2).intersection(label3).intersection(label4).intersection(label5).intersection(label6).intersection(label7).intersection(label8).intersection(label9).intersection(label10)
                      except IndexError:
                        labels = set(label0).intersection(label1).intersection(label2).intersection(label3).intersection(label4).intersection(label5).intersection(label6).intersection(label7).intersection(label8).intersection(label9)
                    except IndexError:
                      labels = set(label0).intersection(label1).intersection(label2).intersection(label3).intersection(label4).intersection(label5).intersection(label6).intersection(label7).intersection(label8)
                  except IndexError:
                    labels = set(label0).intersection(label1).intersection(label2).intersection(label3).intersection(label4).intersection(label5).intersection(label6).intersection(label7)
                except IndexError:
                  labels = set(label0).intersection(label1).intersection(label2).intersection(label3).intersection(label4).intersection(label5).intersection(label6)
              except IndexError:
                labels = set(label0).intersection(label1).intersection(label2).intersection(label3).intersection(label4).intersection(label5)
            except IndexError:
              labels = set(label0).intersection(label1).intersection(label2).intersection(label3).intersection(label4)
          except IndexError:
            labels = set(label0).intersection(label1).intersection(label2).intersection(label3)  
        except IndexError:
          labels = set(label0).intersection(label1).intersection(label2)  
      except IndexError:
        labels = set(label0).intersection(label1)
    except IndexError:
      labels = label0
  except IndexError:
    labels = MealLabel.objects.filter(label=label)

  
  for label in labels:
    servings = label.recipe.servings
    meal_info = [
      label.recipe.id,
      servings,
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

# def generate_plan_meeting_nutrition(meals, nutrition_req):
#   tries = 0
#   while True:
#     tries += 1

#     for i, meal in enumerate(meals):
#       if (i==0):
#         selected_meals = array(choice(meal))
#       else:
#         selected_meals = vstack([selected_meals, array(choice(meal))])

#     met_nutrient_requirement = nutrition_met(selected_meals, nutrition_req)
#     if met_nutrient_requirement:
#       break

#     if tries == MAX_NUMB_OF_INITIAL_MEAL_PLAN_GENERATED:
#       break

#   return selected_meals

# def nutrition_met(plan, nutrition_req):
#   meals_nutrition = get_nutrition(plan)

#   num_of_nutrition_met = 0
#   for i, nutrition_req_amount in enumerate(nutrition_req):
#     # Change code here to set up ranges and around values for nutri
#     if meals_nutrition[i] >= nutrition_req_amount:
#       num_of_nutrition_met += 1
#     # End 

#   if num_of_nutrition_met == len(nutrition_req):
#     return True
#   else:
#     return False

# def get_nutrition(meals):
#     meals_nutrition = [0] * 29

#     for meal in meals:
#       recipe = Recipe.objects.get(id=meal[0])
#       meals_nutrition[0] += recipe.calories / recipe.servings
#       meals_nutrition[1] += recipe.fat / recipe.servings
#       meals_nutrition[2] += recipe.sat_fat / recipe.servings
#       meals_nutrition[3] += recipe.trans_fat / recipe.servings
#       meals_nutrition[4] += recipe.mono_unsat_fat / recipe.servings
#       meals_nutrition[5] += recipe.poly_unsat_fat / recipe.servings
#       meals_nutrition[6] += recipe.carbohydrates / recipe.servings
#       meals_nutrition[7] += recipe.fiber / recipe.servings
#       meals_nutrition[8] += recipe.sugar / recipe.servings
#       meals_nutrition[9] += recipe.protein / recipe.servings
#       meals_nutrition[10] += recipe.cholesterol / recipe.servings
#       meals_nutrition[11] += recipe.sodium / recipe.servings
#       meals_nutrition[12] += recipe.calcium / recipe.servings
#       meals_nutrition[13] += recipe.magnesium / recipe.servings
#       meals_nutrition[14] += recipe.potassium / recipe.servings
#       meals_nutrition[15] += recipe.iron / recipe.servings
#       meals_nutrition[16] += recipe.zinc / recipe.servings
#       meals_nutrition[17] += recipe.phosphorus / recipe.servings
#       meals_nutrition[18] += recipe.vit_a / recipe.servings
#       meals_nutrition[19] += recipe.vit_c / recipe.servings
#       meals_nutrition[20] += recipe.thiamin / recipe.servings
#       meals_nutrition[21] += recipe.riboflavin / recipe.servings
#       meals_nutrition[22] += recipe.niacin / recipe.servings
#       meals_nutrition[23] += recipe.vit_b6 / recipe.servings
#       meals_nutrition[24] += recipe.folic_acid / recipe.servings
#       meals_nutrition[25] += recipe.vit_b12 / recipe.servings
#       meals_nutrition[26] += recipe.vit_d / recipe.servings
#       meals_nutrition[27] += recipe.vit_e / recipe.servings
#       meals_nutrition[28] += recipe.vit_k / recipe.servings      

#     return meals_nutrition