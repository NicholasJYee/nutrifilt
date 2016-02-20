from random import randint
from .models import *

def get_meals(label):
  meals = []
  labels = MealLabel.objects.filter(label=label)

  for label in labels:
    meals.append(label.recipe)

  return meals

def generate_plan_meeting_nutrition(meals, nutrition):
  pass