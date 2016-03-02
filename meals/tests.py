from django.test import TestCase
from meals.models import *

# Create your tests here.
class SimAnnealTestCase(TestCase):
  def setUp(self):
    from numpy import *
    Plan.objects.get_or_create(
      name = "test",
      calories = 2000,
      fat = 0,
      sat_fat = 0,
      trans_fat = 0,
      mono_unsat_fat = 0,
      poly_unsat_fat = 0,
      carbohydrates = 0,
      fiber = 0,
      sugar = 0,
      protein = 0,
      cholesterol = 0,
      sodium = 0,
      calcium = 0,
      magnesium = 0,
      potassium = 0,
      iron = 0,
      zinc = 0,
      phosphorus = 0,
      vit_a = 0,
      vit_c = 0,
      thiamin = 0,
      riboflavin = 0,
      niacin = 0,
      vit_b6 = 0,
      folic_acid = 0,
      vit_b12 = 0,
      vit_d = 0,
      vit_e = 0,
      vit_k = 0
    )

  def test_can_get_recipes(self):
    from .computations import *
    
    breakfast = get_meals('breakfast', health_labels)
    snack = get_meals('snack', health_labels)
    lunch = get_meals('lunch', health_labels)
    dinner = get_meals('dinner', health_labels)

  def test_can_generate_initial_meal_plan(self):
    from .computations import *
    import sim_anneal
    plan5 = array([[ 1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
       0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
       0.,  0.,  0.,  0.,  0.,  0.],
     [ 2.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
       0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
       0.,  0.,  0.,  0.,  0.,  0.],
     [ 3.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
       0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
       0.,  0.,  0.,  0.,  0.,  0.],
     [ 2.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
       0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
       0.,  0.,  0.,  0.,  0.,  0.],
     [ 4.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
       0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
       0.,  0.,  0.,  0.,  0.,  0.]])

    plan6 = array([[ 1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
       0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
       0.,  0.,  0.,  0.,  0.,  0.],
     [ 1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
       0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
       0.,  0.,  0.,  0.,  0.,  0.],
     [ 2.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
       0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
       0.,  0.,  0.,  0.,  0.,  0.],
     [ 3.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
       0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
       0.,  0.,  0.,  0.,  0.,  0.],
     [ 2.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
       0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
       0.,  0.,  0.,  0.,  0.,  0.],
     [ 4.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
       0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
       0.,  0.,  0.,  0.,  0.,  0.]])

    meal_types5 = plan5
    meal_types6 = plan6
    plan5 = asarray(plan5, order='F')
    plan6 = asarray(plan6, order='F')
    meal_types5 = asarray(meal_types5, order='F')
    meal_types6 = asarray(meal_types6, order='F')

    
    sim_anneal.generate_plan_meeting_nutrition(plan, nutrition_req, breakfast, snack, lunch, dinner)