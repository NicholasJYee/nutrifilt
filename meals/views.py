from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect

from .forms import PlanForm
from .computations import *

def demo(request):
  if request.method == 'POST':
    form = PlanForm(request.POST)
    if form.is_valid():
      name = form.cleaned_data['name']
      calories = form.cleaned_data['calories']
      breakfast = get_meals('breakfast')
      snack1 = get_meals('snack')
      lunch = get_meals('lunch')
      snack2 = get_meals('snack')
      dinner = get_meals('dinner')

      meals = [breakfast, snack1, lunch, snack2, dinner]
      nutrition = [calories]
      print(nutrition)
      plan = generate_plan_meeting_nutrition(meals, nutrition)

      return HttpResponseRedirect('/meals/')
  else:
    form = PlanForm()

  return render(request, 'meals/demo.html', {'form': form})

def index(request):
  context = {
    'first_name': "Hatim"
  }
  return render(request, 'meals/index.html', context)