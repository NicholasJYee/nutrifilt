from random import randint, random
from math import ceil, exp
from numpy import array

def sim_anneal(temperature_ini, meal_types, plan, nutrition_req, breakfast, snack, lunch, dinner):
  TEMPERATURE_END = 0.01
  if temperature_ini == 1.:
    TEMPERATURE_NUMB_STEP = 3
    DRAWS = 1
  elif temperature_ini == 5.5:
    TEMPERATURE_NUMB_STEP = 2
    DRAWS = 100
  elif temperature_ini == 10.:
    TEMPERATURE_NUMB_STEP = 1
    DRAWS = 10

  temperature = temperature_ini
  lowest_cost = plan_cost(plan)
  previous_cost = lowest_cost
  cheapest_plan = array(plan)
  num_of_reinitialize = 0
  exit_loops = False

  for i in range(0, TEMPERATURE_NUMB_STEP):
    for j in range(0, DRAWS):
      new_plan, num_of_reinitialize, exit_loops = change_one_meal(num_of_reinitialize, meal_types, plan, nutrition_req, breakfast, snack, lunch, dinner, j, i, DRAWS, TEMPERATURE_NUMB_STEP, exit_loops)
      if exit_loops:
        break

      total_cost = plan_cost(new_plan)

      accept_probablity = min(1., exp(-(total_cost - previous_cost) / temperature))
      rand_accept = random()

      if rand_accept < accept_probablity:
        plan = array(new_plan)
        previous_cost = total_cost

        if total_cost < lowest_cost:
          lowest_cost = total_cost
          cheapest_plan = array(new_plan)

    if exit_loops:
      break
    temperature -= (temperature_ini - TEMPERATURE_END) / TEMPERATURE_NUMB_STEP

  plan = array(cheapest_plan)

  return plan

def change_one_meal(num_of_reinitialize, meal_types, plan, nutrition_req, breakfast, snack, lunch, dinner, draw_num, temp_num, DRAWS, TEMPERATURE_NUMB_STEP, exit_loops):
  if num_of_reinitialize < 3:
    if num_of_reinitialize == 0:
      MAX_NUMB_OF_MEAL_PLAN_GENERATED = 10000
    elif num_of_reinitialize == 1:
      MAX_NUMB_OF_MEAL_PLAN_GENERATED = 5000
    elif num_of_reinitialize ==2:
      MAX_NUMB_OF_MEAL_PLAN_GENERATED = 500
    else:
      raise SystemExit

    for i in range(0, MAX_NUMB_OF_MEAL_PLAN_GENERATED):
      new_plan = array(plan)
      num_meals_to_change = randint(1, int(ceil(float(len(plan)) / 2.)))
      num_meals_to_change = attenuator(num_meals_to_change, draw_num, DRAWS)

      for j in range(0, num_meals_to_change):
        which_meal_to_change = randint(0, len(plan) - 1)
        if int(meal_types[which_meal_to_change, 0]) == 1:
          new_recipe = randint(0, len(breakfast) - 1)
          new_plan[which_meal_to_change,:] = breakfast[new_recipe,:]
        elif int(meal_types[which_meal_to_change, 0]) == 2:
          new_recipe = randint(0, len(snack) - 1)
          new_plan[which_meal_to_change,:] = snack[new_recipe,:]
        elif int(meal_types[which_meal_to_change, 0]) == 3:
          new_recipe = randint(0, len(lunch) - 1)
          new_plan[which_meal_to_change,:] = lunch[new_recipe,:]
        elif int(meal_types[which_meal_to_change, 0]) == 4:
          new_recipe = randint(0, len(dinner) - 1)
          new_plan[which_meal_to_change,:] = dinner[new_recipe,:]

      num_of_nutrition_met = nutrition_met(new_plan, nutrition_req)
      if num_of_nutrition_met == len(nutrition_req):
        break

      if i == MAX_NUMB_OF_MEAL_PLAN_GENERATED - 1:
        print("Couldn't generate another similar plan; trying a new start point")
        new_plan = generate_plan_meeting_nutrition(plan, meal_types, nutrition_req, breakfast, snack, lunch, dinner)
        num_of_reinitialize += 1
        break
  else:
    print("No plan meeting nutritional req :(")
    new_plan = plan
    exit_loops = True

  return new_plan, num_of_reinitialize, exit_loops

def attenuator(num_meals_to_change, iter, max_iter):
  return int(ceil(float(num_meals_to_change) * (2. - exp(float(iter) / (1.5 * float(max_iter))))))

def plan_cost(plan):
  cost = 0.
  for meal in plan:
    cost += meal[2]
  return cost

def generate_plan_meeting_nutrition(plan, meal_types, nutrition_req, breakfast, snack, lunch, dinner):
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
      plan_with_most_nutrition = array(plan)

    if i == MAX_NUMB_OF_MEAL_PLAN_GENERATED - 1:
      print("Can't find plan that met nutrition; using best plan")
      plan = array(plan_with_most_nutrition)

  return plan

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