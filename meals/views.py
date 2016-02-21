from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect

import secret

from .forms import *
from .computations import *

def populate(request):
  if request.method == 'POST':
    form = PopulateForm(request.POST)
    if form.is_valid():
      terms = form.cleaned_data['terms']
      key = {'app_key': secret.app_key, 'app_id': secret.app_id}
      print(key)
      # recipes = requests.get('https://api.edamam.com/search')
      return HttpResponseRedirect('/meals/')
  else:
    form = PopulateForm()

  return render(request, 'meals/populate.html', {'form': form})

def form(request):
  if request.method == 'POST':
    form = PlanForm(request.POST)
    if form.is_valid():
      nutrition_req = {}

      if form.cleaned_data['name'] is not None:
        name = form.cleaned_data['name']
      if form.cleaned_data['calories'] is not None:
        nutrition_req['calories'] = form.cleaned_data['calories']
      if form.cleaned_data['fat'] is not None:
        nutrition_req['fat'] = form.cleaned_data['fat']
      if form.cleaned_data['sat_fat'] is not None:
        nutrition_req['sat_fat'] = form.cleaned_data['sat_fat']
      if form.cleaned_data['trans_fat'] is not None:
        nutrition_req['trans_fat'] = form.cleaned_data['trans_fat']
      if form.cleaned_data['mono_unsat_fat'] is not None:
        nutrition_req['mono_unsat_fat'] = form.cleaned_data['mono_unsat_fat']
      if form.cleaned_data['poly_unsat_fat'] is not None:
        nutrition_req['poly_unsat_fat'] = form.cleaned_data['poly_unsat_fat']
      if form.cleaned_data['carbohydrates'] is not None:
        nutrition_req['carbohydrates'] = form.cleaned_data['carbohydrates']
      if form.cleaned_data['fiber'] is not None:
        nutrition_req['fiber'] = form.cleaned_data['fiber']
      if form.cleaned_data['sugar'] is not None:
        nutrition_req['sugar'] = form.cleaned_data['sugar']
      if form.cleaned_data['protein'] is not None:
        nutrition_req['protein'] = form.cleaned_data['protein']
      if form.cleaned_data['cholesterol'] is not None:
        nutrition_req['cholesterol'] = form.cleaned_data['cholesterol']
      if form.cleaned_data['sodium'] is not None:
        nutrition_req['sodium'] = form.cleaned_data['sodium']
      if form.cleaned_data['calcium'] is not None:
        nutrition_req['calcium'] = form.cleaned_data['calcium']
      if form.cleaned_data['magnesium'] is not None:
        nutrition_req['magnesium'] = form.cleaned_data['magnesium']
      if form.cleaned_data['potassium'] is not None:
        nutrition_req['potassium'] = form.cleaned_data['potassium']
      if form.cleaned_data['iron'] is not None:
        nutrition_req['iron'] = form.cleaned_data['iron']
      if form.cleaned_data['zinc'] is not None:
        nutrition_req['zinc'] = form.cleaned_data['zinc']
      if form.cleaned_data['phosphorus'] is not None:
        nutrition_req['phosphorus'] = form.cleaned_data['phosphorus']
      if form.cleaned_data['vit_a'] is not None:
        nutrition_req['vit_a'] = form.cleaned_data['vit_a']
      if form.cleaned_data['vit_c'] is not None:
        nutrition_req['vit_c'] = form.cleaned_data['vit_c']
      if form.cleaned_data['thiamin'] is not None:
        nutrition_req['thiamin'] = form.cleaned_data['thiamin']
      if form.cleaned_data['riboflavin'] is not None:
        nutrition_req['riboflavin'] = form.cleaned_data['riboflavin']
      if form.cleaned_data['niacin'] is not None:
        nutrition_req['niacin'] = form.cleaned_data['niacin']
      if form.cleaned_data['vit_b6'] is not None:
        nutrition_req['vit_b6'] = form.cleaned_data['vit_b6']
      if form.cleaned_data['folic_acid'] is not None:
        nutrition_req['folic_acid'] = form.cleaned_data['folic_acid']
      if form.cleaned_data['vit_b12'] is not None:
        nutrition_req['vit_b12'] = form.cleaned_data['vit_b12']
      if form.cleaned_data['vit_d'] is not None:
        nutrition_req['vit_d'] = form.cleaned_data['vit_d']
      if form.cleaned_data['vit_e'] is not None:
        nutrition_req['vit_e'] = form.cleaned_data['vit_e']
      if form.cleaned_data['vit_k'] is not None:
        nutrition_req['vit_k'] = form.cleaned_data['vit_k']


      breakfast = get_meals('breakfast')
      snack1 = get_meals('snack')
      lunch = get_meals('lunch')
      snack2 = get_meals('snack')
      dinner = get_meals('dinner')

      meals = [breakfast, snack1, lunch, snack2, dinner]

      plan = generate_plan_meeting_nutrition(meals, nutrition_req)

      return HttpResponseRedirect('/meals/')
  else:
    form = PlanForm()

  return render(request, 'meals/form.html', {'form': form})

def index(request):
  context = {
    'first_name': "Hatim"
  }
  return render(request, 'meals/index.html', context)