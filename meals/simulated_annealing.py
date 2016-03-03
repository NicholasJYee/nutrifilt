from random import randint

def generate_plan_meeting_nutrition(plan, meal_types, untouched_plan, nutrition_req, breakfast, snack, lunch, dinner):
  MAX_NUMB_OF_MEAL_PLAN_GENERATED = 10000

  most_nutrient_met = 0

  for i in range(0, MAX_NUMB_OF_MEAL_PLAN_GENERATED):
    for j, meal_type in enumerate(meal_types):
      if meal_type[0] == 1:
        meal_number = randint(0, len(breakfast) - 1)
        plan[j] = breakfast[meal_number]
      elif meal_type[0] == 2:
        meal_number = randint(0, len(snack) - 1)
        plan[j] = snack[meal_number]
      elif meal_type[0] == 3:
        meal_number = randint(0, len(lunch) - 1)
        plan[j] = lunch[meal_number]
      elif meal_type[0] == 4:
        meal_number = randint(0, len(dinner) - 1)
        plan[j] = dinner[meal_number]

    num_of_nutrition_met = nutrition_met(plan, nutrition_req)
    if num_of_nutrition_met == len(nutrition_req):
      break
    elif num_of_nutrition_met >= most_nutrient_met:
      most_nutrient_met = num_of_nutrition_met
      plan_with_most_nutrition = plan


def nutrition_met(plan, nutrition_req):
  num_of_nutrition_met = 0
  meals_nutrition = get_nutrition(plan)

  for i, nutrition in enumerate(nutrition_req):
    if nutrition != 0.:
      if (meals_nutrition[i] >= nutrition * 0.8) and (meals_nutrition[i] <= nutrition * 1.2):
        num_of_nutrition_met += 1
    else:
      num_of_nutrition_met += 1

  return num_of_nutrition_met   

def get_nutrition(plan):
  meals_nutrition = [0] * 29

  for meal in plan:
    meals_nutrition[0] += meal[3]
    meals_nutrition[1] += meal[4]
    meals_nutrition[2] += meal[5]
    meals_nutrition[3] += meal[6]
    meals_nutrition[4] += meal[7]
    meals_nutrition[5] += meal[8]
    meals_nutrition[6] += meal[9]
    meals_nutrition[7] += meal[10]
    meals_nutrition[8] += meal[11]
    meals_nutrition[9] += meal[12]
    meals_nutrition[10] += meal[13]
    meals_nutrition[11] += meal[14]
    meals_nutrition[12] += meal[15]
    meals_nutrition[13] += meal[16]
    meals_nutrition[14] += meal[17]
    meals_nutrition[15] += meal[18]
    meals_nutrition[16] += meal[19]
    meals_nutrition[17] += meal[20]
    meals_nutrition[18] += meal[21]
    meals_nutrition[19] += meal[22]
    meals_nutrition[20] += meal[23]
    meals_nutrition[21] += meal[24]
    meals_nutrition[22] += meal[25]
    meals_nutrition[23] += meal[26]
    meals_nutrition[24] += meal[27]
    meals_nutrition[25] += meal[28]
    meals_nutrition[26] += meal[29]
    meals_nutrition[27] += meal[30]
    meals_nutrition[28] += meal[31]

  return meals_nutrition