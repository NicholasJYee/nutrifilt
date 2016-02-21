from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect

from .forms import PlanForm
from .computations import *

def demo(request):
  if request.method == 'POST':
    form = PlanForm(request.POST)
    if form.is_valid():
      nutrition_req = {}

      name = form.cleaned_data['name']
      if form.cleaned_data['calories'] is not None:
        nutrition_req['calories'] = form.cleaned_data['calories']
      if form.cleaned_data['fat'] is not None:
        nutrition_req['fat'] = form.cleaned_data['fat']


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

  return render(request, 'meals/demo.html', {'form': form})

def index(request):
  context = {
    'first_name': "Hatim"
  }
  return render(request, 'meals/index.html', context)