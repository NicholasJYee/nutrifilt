from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from numpy import array, asarray, size, append
import requests, time
from scipy import optimize

import secret

from .forms import *
from .computations import *
import sim_anneal

def searchplan(request):
  try:
    context = {
      'plan': Plan.objects.get(name=request.GET.get('name', ''))
    }
  except:
    context = {}
  return render(request, 'meals/plan.html', context)

class MealPlanStep(object):
  def __call__(self, plan):
    change_one_meal(plan)
    return plan

def change_one_meal(plan):
  tries = 0

  for i in range(0,5):
    start = i * 32
    end = (i + 1) * 32
    if (i == 0):
      restored_2d_plan = array(plan[start:end])
    else:
      restored_2d_plan = vstack([restored_2d_plan, array(plan[start:end])])
  plan = restored_2d_plan

  original_plan = plan
  while True:
    tries += 1
    changed_meal = randint(0, 4)

    if (changed_meal == 0):
      plan[changed_meal] = choice(breakfast)
    elif (changed_meal == 1):
      plan[changed_meal] = choice(snack)
    elif (changed_meal == 2):
      plan[changed_meal] = choice(lunch)
    elif (changed_meal == 3):
      plan[changed_meal] = choice(snack)
    elif (changed_meal == 4):
      plan[changed_meal] = choice(dinner)

    met_nutrient_requirement = nutrition_met(plan, nutrition_req)
    if met_nutrient_requirement:
      break

    if tries == MAX_NUMB_OF_INITIAL_MEAL_PLAN_GENERATED:
        break
    plan = original_plan

def plan_cost(plan):
  cost = 0
  for recipe_num in plan[::32]:
    recipe = Recipe.objects.get(id=int(recipe_num))
    cost += recipe.cost / recipe.servings
  return float("{0:.2f}".format(cost))

def plan(request, plan_id):
  try:
    context = {
      'plan': Plan.objects.get(id=int(plan_id))
    }
  except:
    context = {}  
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
  get_recipe_cost(Recipe.objects.all())#filter(cost__isnull=True))
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

def get_recipe_cost(recipes):
  for recipe in recipes:
    cost = 0
    for ingredientrecipe in recipe.ingredientrecipe_set.all():
      ingredient_price = ingredientrecipe.ingredient.ingredientvendor_set.first().price
      weight_used = ingredientrecipe.weight
      ingredient_weight = ingredientrecipe.ingredient.ingredientvendor_set.first().weight
      cost += ingredient_price * weight_used / ingredient_weight
    recipe.cost = ("%.2f" % round(cost,2))
    recipe.save()

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

    if "ground pepper" in ingredientrecipe.food:
      ingredientrecipe.ingredient = Ingredient.objects.get(food="pepper")
      ingredientrecipe.save()

    if "vanilla" in ingredientrecipe.food:
      ingredientrecipe.ingredient = Ingredient.objects.get(food="vanilla extract")
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

      if form.cleaned_data['name'] is not None:
        name = form.cleaned_data['name']

      global nutrition_req
      global breakfast
      global snack
      global lunch
      global dinner
      nutrition_req = get_nutrition_req(form)
      breakfast = get_meals('breakfast')
      snack = get_meals('snack')
      lunch = get_meals('lunch')
      dinner = get_meals('dinner')

      # # For Basinhopping
      # meals = [breakfast, snack, lunch, snack, dinner]
      # mealplanstep = MealPlanStep()
      # x0 = generate_plan_meeting_nutrition(meals, nutrition_req)
      # plan = optimize.basinhopping(plan_cost, x0, take_step=mealplanstep, niter=1).x

      # For Sim Annealing (Fortran)
        # 1 - breakfast
        # 2 - snack
        # 3 - lunch
        # 4 - dinner
      zero_31_times = [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]
      first = append(1., [zero_31_times])
      second = append(2., [zero_31_times])
      third = append(3., [zero_31_times])
      fourth = append(2., [zero_31_times])
      fifth = append(4., [zero_31_times])

      plan = array([first, second, third, fourth, fifth], 'd')
      plan = asarray(plan, order='F')
      print("plan: (before sim): ", plan)
      sim_anneal.generate_plan_meeting_nutrition(plan, nutrition_req, breakfast, snack, lunch, dinner)
      print("plan: (after sim)", plan)
      raise SystemExit



      p, created = Plan.objects.get_or_create(
        name = name,
        calories = nutrition_req[0],
        fat = nutrition_req[1],
        sat_fat = nutrition_req[2],
        trans_fat = nutrition_req[3],
        mono_unsat_fat = nutrition_req[4],
        poly_unsat_fat = nutrition_req[5],
        carbohydrates = nutrition_req[6],
        fiber = nutrition_req[7],
        sugar = nutrition_req[8],
        protein = nutrition_req[9],
        cholesterol = nutrition_req[10],
        sodium = nutrition_req[11],
        calcium = nutrition_req[12],
        magnesium = nutrition_req[13],
        potassium = nutrition_req[14],
        iron = nutrition_req[15],
        zinc = nutrition_req[16],
        phosphorus = nutrition_req[17],
        vit_a = nutrition_req[18],
        vit_c = nutrition_req[19],
        thiamin = nutrition_req[20],
        riboflavin = nutrition_req[21],
        niacin = nutrition_req[22],
        vit_b6 = nutrition_req[23],
        folic_acid = nutrition_req[24],
        vit_b12 = nutrition_req[25],
        vit_d = nutrition_req[26],
        vit_e = nutrition_req[27],
        vit_k = nutrition_req[28]
      )

      if created:
        for i in range(0,5):
          start = i * 32
          end = (i + 1) * 32
          if (i == 0):
            restored_2d_plan = array(plan[start:end])
          else:
            restored_2d_plan = vstack([restored_2d_plan, array(plan[start:end])])
        plan = restored_2d_plan[::-1]

        for i, meal in enumerate(plan):
          recipe = Recipe.objects.get(id=meal[0])
          p.planrecipe_set.get_or_create(
            recipe = recipe,
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

#Meal plan results front-end test
# def results(request):
#   return render(request, 'meals/results.html')  