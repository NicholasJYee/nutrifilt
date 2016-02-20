from random import randint, choice
from .models import *

def get_meals(label):
  meals = []
  labels = MealLabel.objects.filter(label=label)

  for label in labels:
    meals.append(label.recipe)

  return meals

def generate_plan_meeting_nutrition(meals, nutrition):
  for i, meal in enumerate(meals):
    meals[i] = choice(meals[i])
    print(meals[i])
  return meals