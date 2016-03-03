from random import randint

def generate_plan_meeting_nutrition(plan, nutrition_req, breakfast, snack, lunch, dinner):
  MAX_NUMB_OF_MEAL_PLAN_GENERATED = 1000

  most_nutrient_met = 0

  for i in range(0, MAX_NUMB_OF_MEAL_PLAN_GENERATED):
    for j, meal in enumerate(plan):
      if meal[0] == 1:
        randint(0, len(breakfast))
        print("breakfast")
      elif meal[0] == 2:
        randint(0, len(snack))
        print("snack")
      elif meal[0] == 3:
        randint(0, len(lunch))
        print("lunch")
      elif meal[0] == 4:
        randint(0, len(dinner))
        print("dinner")
