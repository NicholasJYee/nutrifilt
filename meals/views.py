from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
import requests

import secret

from .forms import *
from .computations import *

def plan(request, plan_id):
  context = {
    'plan': Plan.objects.get(id=int(plan_id))
  }
  return render(request, 'meals/plan.html', context)

def populate(request):
  if request.method == 'POST':
    form = PopulateForm(request.POST)
    if form.is_valid():
      terms = form.cleaned_data['terms']
      payload = {
        'app_key': secret.app_key,
        'app_id': secret.app_id,
        'q': terms,
        'to': 5
      }
      recipes = requests.get('https://api.edamam.com/search', params=payload).json()
      store_recipes(recipes)
      return HttpResponseRedirect('/meals/populate/')
  else:
    form = PopulateForm()

  try_assigning_ingredientrecipe_with_ingredient(IngredientRecipe.objects.filter(ingredient__isnull=True))
  recipes_without_meal_labels = Recipe.objects.filter(meallabel__isnull=True)
  ingredientrecipe_without_ingredients = IngredientRecipe.objects.filter(ingredient__isnull=True)
  ingredient_without_ingredientvendor = Ingredient.objects.filter(ingredientvendor__isnull=True)

  context = {
    'form': form,
    'recipes_without_meal_labels': recipes_without_meal_labels,
    'ingredientrecipe_without_ingredients': ingredientrecipe_without_ingredients,
    'ingredient_without_ingredientvendor': ingredient_without_ingredientvendor
  }
  return render(request, 'meals/populate.html', context)

def try_assigning_ingredientrecipe_with_ingredient(ingredientrecipes):
  ingredients = Ingredient.objects.all()

  for ingredientrecipe in ingredientrecipes:
    if ingredientrecipe.food == "ice":
      ingredientrecipe.ingredient = Ingredient.objects.get(food="water")
      ingredientrecipe.save()

    if "sugar" in ingredientrecipe.food:
      ingredientrecipe.ingredient = Ingredient.objects.get(food="sugar")
      ingredientrecipe.save()

    if "salt" in ingredientrecipe.food:
      ingredientrecipe.ingredient = Ingredient.objects.get(food="salt")
      ingredientrecipe.save()

    if "olive oil" in ingredientrecipe.food:
      ingredientrecipe.ingredient = Ingredient.objects.get(food="olive oil")
      ingredientrecipe.save()

    if "yellow onion" in ingredientrecipe.food:
      ingredientrecipe.ingredient = Ingredient.objects.get(food="yellow onion")
      ingredientrecipe.save()

    if "white vinegar" in ingredientrecipe.food:
      ingredientrecipe.ingredient = Ingredient.objects.get(food="vinegar")
      ingredientrecipe.save()

    for ingredient in ingredients:
      if (ingredientrecipe.food == ingredient.food) or (ingredientrecipe.food == ingredient.food + "s"):
        ingredientrecipe.ingredient = ingredient
        ingredientrecipe.save()



def store_recipes(recipes):
  for recipe in recipes[u'hits']:
    recipe = recipe[u'recipe']

    r = create_recipe(recipe)

    for ingredient in recipe[u'ingredients']:
      r.ingredientrecipe_set.get_or_create(
        text = ingredient[u'text'].encode('utf-8'),
        food = ingredient[u'food'].encode('utf-8'),
        weight = str(float(ingredient[u'weight']))
      )

    for healthlabel in recipe[u'healthLabels']:
      r.healthlabel_set.get_or_create(label = healthlabel)

def create_recipe(recipe):
  try:
    image = recipe[u'image'].encode('utf-8')
  except KeyError:
    image = ""
  try:
    url = recipe[u'url'].encode('utf-8')
  except KeyError:
    url = ""
  try:
    servings = float(str(recipe[u'yield']))
  except KeyError:
    servings = 0
  try:
    calories = float(str(recipe[u'totalNutrients'][u'ENERC_KCAL'][u'quantity']))
  except KeyError:
    calories = 0
  try:
    fat = float(str(recipe[u'totalNutrients'][u'FAT'][u'quantity']))
  except KeyError:
    fat = 0
  try:
    sat_fat = float(str(recipe[u'totalNutrients'][u'FASAT'][u'quantity']))
  except KeyError:
    sat_fat = 0
  try:
    trans_fat = float(str(recipe[u'totalNutrients'][u'FATRN'][u'quantity']))
  except KeyError:
    trans_fat = 0
  try:
    mono_unsat_fat = float(str(recipe[u'totalNutrients'][u'FAMS'][u'quantity']))
  except KeyError:
    mono_unsat_fat = 0
  try:
    poly_unsat_fat = float(str(recipe[u'totalNutrients'][u'FAPU'][u'quantity']))
  except KeyError:
    poly_unsat_fat = 0
  try:
    carbohydrates = float(str(recipe[u'totalNutrients'][u'CHOCDF'][u'quantity']))
  except KeyError:
    carbohydrates = 0
  try:
    fiber = float(str(recipe[u'totalNutrients'][u'FIBTG'][u'quantity']))
  except KeyError:
    fiber = 0
  try:
    sugar = float(str(recipe[u'totalNutrients'][u'SUGAR'][u'quantity']))
  except KeyError:
    sugar = 0
  try:
    protein = float(str(recipe[u'totalNutrients'][u'PROCNT'][u'quantity']))
  except KeyError:
    protein = 0
  try:
    cholesterol = float(str(recipe[u'totalNutrients'][u'CHOLE'][u'quantity']))
  except KeyError:
    cholesterol = 0
  try:
    sodium = float(str(recipe[u'totalNutrients'][u'NA'][u'quantity']))
  except KeyError:
    sodium = 0
  try:
    calcium = float(str(recipe[u'totalNutrients'][u'CA'][u'quantity']))
  except KeyError:
    calcium = 0
  try:
    magnesium = float(str(recipe[u'totalNutrients'][u'MG'][u'quantity']))
  except KeyError:
    magnesium = 0
  try:
    potassium = float(str(recipe[u'totalNutrients'][u'K'][u'quantity']))
  except KeyError:
    potassium = 0
  try:
    iron = float(str(recipe[u'totalNutrients'][u'FE'][u'quantity']))
  except KeyError:
    iron = 0
  try:
    zinc = float(str(recipe[u'totalNutrients'][u'ZN'][u'quantity']))
  except KeyError:
    zinc = 0
  try:
    phosphorus = float(str(recipe[u'totalNutrients'][u'P'][u'quantity']))
  except KeyError:
    phosphorus = 0
  try:
    vit_a = float(str(recipe[u'totalNutrients'][u'VITA_RAE'][u'quantity']))
  except KeyError:
    vit_a = 0
  try:
    vit_c = float(str(recipe[u'totalNutrients'][u'VITC'][u'quantity']))
  except KeyError:
    vit_c = 0
  try:
    thiamin = float(str(recipe[u'totalNutrients'][u'THIA'][u'quantity']))
  except KeyError:
    thiamin = 0
  try:
    riboflavin = float(str(recipe[u'totalNutrients'][u'RIBF'][u'quantity']))
  except KeyError:
    riboflavin = 0
  try:
    niacin = float(str(recipe[u'totalNutrients'][u'NIA'][u'quantity']))
  except KeyError:
    niacin = 0
  try:
    vit_b6 = float(str(recipe[u'totalNutrients'][u'VITB6A'][u'quantity']))
  except KeyError:
    vit_b6 = 0
  try:
    folic_acid = float(str(recipe[u'totalNutrients'][u'FOL'][u'quantity']))
  except KeyError:
    folic_acid = 0
  try:
    vit_b12 = float(str(recipe[u'totalNutrients'][u'VITB12'][u'quantity']))
  except KeyError:
    vit_b12 = 0
  try:
    vit_d = float(str(recipe[u'totalNutrients'][u'VITD'][u'quantity']))
  except KeyError:
    vit_d = 0
  try:
    vit_e = float(str(recipe[u'totalNutrients'][u'TOCPHA'][u'quantity']))
  except KeyError:
    vit_e = 0
  try:
    vit_k = float(str(recipe[u'totalNutrients'][u'VITK1'][u'quantity']))
  except KeyError:
    vit_k = 0

  r, created = Recipe.objects.get_or_create(
    label = recipe[u'label'].encode('utf-8'),
  )

  if created:
    r.delete()
    r, created = Recipe.objects.get_or_create(
      label = str(recipe[u'label']),
      image = image,
      url = url,
      servings = servings,
      calories = calories,
      fat = fat,
      sat_fat = sat_fat,
      trans_fat = trans_fat,
      mono_unsat_fat = mono_unsat_fat,
      poly_unsat_fat = poly_unsat_fat,
      carbohydrates = carbohydrates,
      fiber = fiber,
      sugar = sugar,
      protein = protein,
      cholesterol = cholesterol,
      sodium = sodium,
      calcium = calcium,
      magnesium = magnesium,
      potassium = potassium,
      iron = iron,
      zinc = zinc,
      phosphorus = phosphorus,
      vit_a = vit_a,
      vit_c = vit_c,
      thiamin = thiamin,
      riboflavin = riboflavin,
      niacin = niacin,
      vit_b6 = vit_b6,
      folic_acid = folic_acid,
      vit_b12 = vit_b12,
      vit_d = vit_d,
      vit_e = vit_e,
      vit_k = vit_k
    )

  return r

def form(request):
  if request.method == 'POST':
    form = PlanForm(request.POST)
    if form.is_valid():
      nutrition_req = {}

      if form.cleaned_data['name'] is not None:
        name = form.cleaned_data['name']
      if form.cleaned_data['calories'] is not None:
        nutrition_req['calories'] = form.cleaned_data['calories']
      else:
        nutrition_req['calories'] = 0
      if form.cleaned_data['fat'] is not None:
        nutrition_req['fat'] = form.cleaned_data['fat']
      else:
        nutrition_req['fat'] = 0
      if form.cleaned_data['sat_fat'] is not None:
        nutrition_req['sat_fat'] = form.cleaned_data['sat_fat']
      else:
        nutrition_req['sat_fat'] = 0
      if form.cleaned_data['trans_fat'] is not None:
        nutrition_req['trans_fat'] = form.cleaned_data['trans_fat']
      else:
        nutrition_req['trans_fat'] = 0
      if form.cleaned_data['mono_unsat_fat'] is not None:
        nutrition_req['mono_unsat_fat'] = form.cleaned_data['mono_unsat_fat']
      else:
        nutrition_req['mono_unsat_fat'] = 0
      if form.cleaned_data['poly_unsat_fat'] is not None:
        nutrition_req['poly_unsat_fat'] = form.cleaned_data['poly_unsat_fat']
      else:
        nutrition_req['poly_unsat_fat'] = 0
      if form.cleaned_data['carbohydrates'] is not None:
        nutrition_req['carbohydrates'] = form.cleaned_data['carbohydrates']
      else:
        nutrition_req['carbohydrates'] = 0
      if form.cleaned_data['fiber'] is not None:
        nutrition_req['fiber'] = form.cleaned_data['fiber']
      else:
        nutrition_req['fiber'] = 0
      if form.cleaned_data['sugar'] is not None:
        nutrition_req['sugar'] = form.cleaned_data['sugar']
      else:
        nutrition_req['sugar'] = 0
      if form.cleaned_data['protein'] is not None:
        nutrition_req['protein'] = form.cleaned_data['protein']
      else:
        nutrition_req['protein'] = 0
      if form.cleaned_data['cholesterol'] is not None:
        nutrition_req['cholesterol'] = form.cleaned_data['cholesterol']
      else:
        nutrition_req['cholesterol'] = 0
      if form.cleaned_data['sodium'] is not None:
        nutrition_req['sodium'] = form.cleaned_data['sodium']
      else:
        nutrition_req['sodium'] = 0
      if form.cleaned_data['calcium'] is not None:
        nutrition_req['calcium'] = form.cleaned_data['calcium']
      else:
        nutrition_req['calcium'] = 0
      if form.cleaned_data['magnesium'] is not None:
        nutrition_req['magnesium'] = form.cleaned_data['magnesium']
      else:
        nutrition_req['magnesium'] = 0
      if form.cleaned_data['potassium'] is not None:
        nutrition_req['potassium'] = form.cleaned_data['potassium']
      else:
        nutrition_req['potassium'] = 0
      if form.cleaned_data['iron'] is not None:
        nutrition_req['iron'] = form.cleaned_data['iron']
      else:
        nutrition_req['iron'] = 0
      if form.cleaned_data['zinc'] is not None:
        nutrition_req['zinc'] = form.cleaned_data['zinc']
      else:
        nutrition_req['zinc'] = 0
      if form.cleaned_data['phosphorus'] is not None:
        nutrition_req['phosphorus'] = form.cleaned_data['phosphorus']
      else:
        nutrition_req['phosphorus'] = 0
      if form.cleaned_data['vit_a'] is not None:
        nutrition_req['vit_a'] = form.cleaned_data['vit_a']
      else:
        nutrition_req['vit_a'] = 0
      if form.cleaned_data['vit_c'] is not None:
        nutrition_req['vit_c'] = form.cleaned_data['vit_c']
      else:
        nutrition_req['vit_c'] = 0
      if form.cleaned_data['thiamin'] is not None:
        nutrition_req['thiamin'] = form.cleaned_data['thiamin']
      else:
        nutrition_req['thiamin'] = 0
      if form.cleaned_data['riboflavin'] is not None:
        nutrition_req['riboflavin'] = form.cleaned_data['riboflavin']
      else:
        nutrition_req['riboflavin'] = 0
      if form.cleaned_data['niacin'] is not None:
        nutrition_req['niacin'] = form.cleaned_data['niacin']
      else:
        nutrition_req['niacin'] = 0
      if form.cleaned_data['vit_b6'] is not None:
        nutrition_req['vit_b6'] = form.cleaned_data['vit_b6']
      else:
        nutrition_req['vit_b6'] = 0
      if form.cleaned_data['folic_acid'] is not None:
        nutrition_req['folic_acid'] = form.cleaned_data['folic_acid']
      else:
        nutrition_req['folic_acid'] = 0
      if form.cleaned_data['vit_b12'] is not None:
        nutrition_req['vit_b12'] = form.cleaned_data['vit_b12']
      else:
        nutrition_req['vit_b12'] = 0
      if form.cleaned_data['vit_d'] is not None:
        nutrition_req['vit_d'] = form.cleaned_data['vit_d']
      else:
        nutrition_req['vit_d'] = 0
      if form.cleaned_data['vit_e'] is not None:
        nutrition_req['vit_e'] = form.cleaned_data['vit_e']
      else:
        nutrition_req['vit_e'] = 0
      if form.cleaned_data['vit_k'] is not None:
        nutrition_req['vit_k'] = form.cleaned_data['vit_k']
      else:
        nutrition_req['vit_k'] = 0

      breakfast = get_meals('breakfast')
      snack1 = get_meals('snack')
      lunch = get_meals('lunch')
      snack2 = get_meals('snack')
      dinner = get_meals('dinner')

      meals = [breakfast, snack1, lunch, snack2, dinner]

      plan = generate_plan_meeting_nutrition(meals, nutrition_req)

      p, created = Plan.objects.get_or_create(
        name = name,
        calories = nutrition_req['calories'],
        fat = nutrition_req['fat'],
        sat_fat = nutrition_req['sat_fat'],
        trans_fat = nutrition_req['trans_fat'],
        mono_unsat_fat = nutrition_req['mono_unsat_fat'],
        poly_unsat_fat = nutrition_req['poly_unsat_fat'],
        carbohydrates = nutrition_req['carbohydrates'],
        fiber = nutrition_req['fiber'],
        sugar = nutrition_req['sugar'],
        protein = nutrition_req['protein'],
        cholesterol = nutrition_req['cholesterol'],
        sodium = nutrition_req['sodium'],
        calcium = nutrition_req['calcium'],
        magnesium = nutrition_req['magnesium'],
        potassium = nutrition_req['potassium'],
        iron = nutrition_req['iron'],
        zinc = nutrition_req['zinc'],
        phosphorus = nutrition_req['phosphorus'],
        vit_a = nutrition_req['vit_a'],
        vit_c = nutrition_req['vit_c'],
        thiamin = nutrition_req['thiamin'],
        riboflavin = nutrition_req['riboflavin'],
        niacin = nutrition_req['niacin'],
        vit_b6 = nutrition_req['vit_b6'],
        folic_acid = nutrition_req['folic_acid'],
        vit_b12 = nutrition_req['vit_b12'],
        vit_d = nutrition_req['vit_d'],
        vit_e = nutrition_req['vit_e'],
        vit_k = nutrition_req['vit_k']
      )

      if created:
        for i, meal in enumerate(plan):
          p.planrecipe_set.get_or_create(
            recipe = meal,
            meal_number = i
          )

      return HttpResponseRedirect('/meals/plan/' + str(p.id))
  else:
    form = PlanForm()

  context = {
    'form': form,
    'plans': Plan.objects.all()
  }
  return render(request, 'meals/form.html', context)

def index(request):
  context = {
    'first_name': "Hatim"
  }
  return render(request, 'meals/index.html', context)

#modified demo to reflect in search form
def search(request):
  if request.method == 'POST':
    form = PlanForm(request.POST)
    if form.is_valid():
      name = form.cleaned_data['name']
      calories = form.cleaned_data['calories']

      return HttpResponseRedirect('/meals/')
  else:
    form = PlanForm()

  return render(request, 'meals/search.html', {'form': form})