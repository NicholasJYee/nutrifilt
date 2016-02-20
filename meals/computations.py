from .models import *

def get_meals(label):
  meals = []
  labels = MealLabel.objects.filter(label=label)
  
  
  return meals