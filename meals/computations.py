from .models import *

def get_meals(label):
  meals = []
  labels = MealLabel.objects.filter(label=label)
  print("hi")
  print(labels)

  return labels