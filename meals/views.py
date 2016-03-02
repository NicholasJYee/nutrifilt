from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from numpy import array, asarray, size, append
import requests, time
from scipy import optimize
from collections import defaultdict

import secret

from .forms import *
from .computations import *
import sim_anneal

def plan_info(plan):
  try:    
    calories = format(sum(meal.recipe.calories/meal.recipe.servings for meal in plan.planrecipe_set.all()), '.1f')
    fat = format(sum(meal.recipe.fat/meal.recipe.servings for meal in plan.planrecipe_set.all()), '.1f')
    carbohydrates = format(sum(meal.recipe.carbohydrates/meal.recipe.servings for meal in plan.planrecipe_set.all()), '.1f')
    protein = format(sum(meal.recipe.protein/meal.recipe.servings for meal in plan.planrecipe_set.all()), '.1f')    
    extras = []
    ingredients = plan.make_grocery_list()
    
    if plan.sat_fat > 0:
      extras.append(["Saturated Fat (g)", plan.sat_fat, format(sum(meal.recipe.sat_fat/meal.recipe.servings for meal in plan.planrecipe_set.all()), '.1f') ])
    
    if plan.trans_fat > 0:  
      extras.append(["Trans Fat (g)", plan.trans_fat, format(sum(meal.recipe.trans_fat/meal.recipe.servings for meal in plan.planrecipe_set.all()), '.1f') ])
    
    if plan.mono_unsat_fat > 0:   
      extras.append(["Monounsaturated Fat (g)", plan.mono_unsat_fat, format(sum(meal.recipe.mono_unsat_fat/meal.recipe.servings for meal in plan.planrecipe_set.all()), '.1f') ])  
    
    if plan.poly_unsat_fat > 0:
      extras.append(["Polyunsaturated Fat (g)", plan.poly_unsat_fat, format(sum(meal.recipe.poly_unsat_fat/meal.recipe.servings for meal in plan.planrecipe_set.all()), '.1f') ])

    if plan.fiber > 0:
      extras.append(["Fiber (g)", plan.fiber, format(sum(meal.recipe.fiber/meal.recipe.servings for meal in plan.planrecipe_set.all()), '.1f') ])  
    
    if plan.sugar > 0:
      extras.append(["Sugar (g)", plan.sugar, format(sum(meal.recipe.sugar/meal.recipe.servings for meal in plan.planrecipe_set.all()), '.1f') ])  
    
    if plan.cholesterol > 0:
      extras.append(["Cholesterol (mg)", plan.cholesterol, format(sum(meal.recipe.cholesterol/meal.recipe.servings for meal in plan.planrecipe_set.all()), '.1f') ])  
    
    if  plan.sodium > 0:
      extras.append(["Sodium (mg)", plan.sodium, format(sum(meal.recipe.sodium/meal.recipe.servings for meal in plan.planrecipe_set.all()), '.1f') ])
    
    if  plan.calcium > 0:
      extras.append(["Calcium (mg)", plan.calcium, format(sum(meal.recipe.calcium/meal.recipe.servings for meal in plan.planrecipe_set.all()), '.1f') ])
    
    if  plan.magnesium > 0:
      extras.append(["Magnesium (mg)", plan.magnesium, format(sum(meal.recipe.magnesium/meal.recipe.servings for meal in plan.planrecipe_set.all()), '.1f') ])
    
    if  plan.potassium > 0:
      extras.append(["Potassium (mg)", plan.potassium, format(sum(meal.recipe.potassium/meal.recipe.servings for meal in plan.planrecipe_set.all()), '.1f') ])
    
    if  plan.iron > 0:
      extras.append(["Iron (mg)", plan.iron, format(sum(meal.recipe.iron/meal.recipe.servings for meal in plan.planrecipe_set.all()), '.1f') ])
    
    if  plan.zinc > 0:
      extras.append(["Zinc (mg)", plan.zinc, format(sum(meal.recipe.zinc/meal.recipe.servings for meal in plan.planrecipe_set.all()), '.1f') ])
    
    if  plan.phosphorus > 0:
      extras.append(["Phosphorus (mg)", plan.phosphorus, format(sum(meal.recipe.phosphorus/meal.recipe.servings for meal in plan.planrecipe_set.all()), '.1f') ])
    
    if  plan.vit_a > 0:
      extras.append(["Vitamin A (micro g)", plan.vit_a, format(sum(meal.recipe.vit_a/meal.recipe.servings for meal in plan.planrecipe_set.all()), '.1f') ])
    
    if  plan.vit_c > 0:
      extras.append(["Vitamin C (mg)", plan.vit_c, format(sum(meal.recipe.vit_c/meal.recipe.servings for meal in plan.planrecipe_set.all()), '.1f') ])
    
    if  plan.thiamin > 0:
      extras.append(["Thiamin (mg)", plan.thiamin, format(sum(meal.recipe.thiamin/meal.recipe.servings for meal in plan.planrecipe_set.all()), '.1f') ])
    
    if  plan.riboflavin > 0:
      extras.append(["Riboflavin (mg)", plan.riboflavin, format(sum(meal.recipe.riboflavin/meal.recipe.servings for meal in plan.planrecipe_set.all()), '.1f') ])
    
    if  plan.niacin > 0:
      extras.append(["Niacin (mg)", plan.niacin, format(sum(meal.recipe.niacin/meal.recipe.servings for meal in plan.planrecipe_set.all()), '.1f') ])
    
    if  plan.vit_b6 > 0:
      extras.append(["Vitamin B6 (mg)", plan.vit_b6, format(sum(meal.recipe.vit_b6/meal.recipe.servings for meal in plan.planrecipe_set.all()), '.1f') ])
    
    if  plan.folic_acid > 0:
      extras.append(["Folic Acid (micro g)", plan.folic_acid, format(sum(meal.recipe.folic_acid/meal.recipe.servings for meal in plan.planrecipe_set.all()), '.1f') ])
    
    if  plan.vit_b12 > 0:
      extras.append(["Vitamin B12 (micro g)", plan.vit_b12, format(sum(meal.recipe.vit_b12/meal.recipe.servings for meal in plan.planrecipe_set.all()), '.1f') ])
    
    if  plan.vit_d > 0:
      extras.append(["Vitamin D (micro g)", plan.vit_d, format(sum(meal.recipe.vit_d/meal.recipe.servings for meal in plan.planrecipe_set.all()), '.1f') ])
    
    if  plan.vit_e > 0:
      extras.append(["Vitamin E (mg)", plan.vit_e, format(sum(meal.recipe.vit_e/meal.recipe.servings for meal in plan.planrecipe_set.all()), '.1f') ])
    
    if  plan.vit_k > 0:
      extras.append(["Vitamin K (micro g)", plan.vit_k, format(sum(meal.recipe.vit_k/meal.recipe.servings for meal in plan.planrecipe_set.all()), '.1f') ])       
    
            
    context = {
      'plan': plan,
      'calories': calories,
      'fat' : fat,
      'carbohydrates' : carbohydrates,
      'protein' : protein,
      'extras' : extras,
      'ingredients' : ingredients
    }
  except:
    context = {}
  return context

#Search plan by name
def searchplan(request):
  plan = Plan.objects.get(name=request.GET.get('name', ''))  
  return render(request, 'meals/plan.html', plan_info(plan))

#search plan by id
def plan(request, plan_id):
  plan = Plan.objects.get(id=int(plan_id))
  return render(request, 'meals/plan.html', plan_info(plan))

def weekly_plan(request, plan_id):
  weekly_plan = []
  plans = list(Plan.objects.filter(id__in=range(int(plan_id), int(plan_id) + 7)))
  for i, plan in enumerate(plans):
    weekly_plan.append(plan_info(plan))
  return render(request, 'meals/weekly_plan.html', {"plans": weekly_plan})

class MealPlanStep(object):
  def __call__(self, plan):
    plan = change_one_meal(plan)
    return plan

def change_one_meal(plan):
  print("Changing plan")
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

  return plan

def plan_cost(plan):
  cost = 0
  for recipe_num in plan[::32]:
    recipe = Recipe.objects.get(id=int(recipe_num))
    cost += recipe.cost / recipe.servings
  print("Cost: ", float("{0:.2f}".format(cost)))
  return float("{0:.2f}".format(cost))

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

def select_meal_type(type_of_meal):
  zero_31_times = [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]
  breakfast_meal_type = append(1., [zero_31_times])
  snack_meal_type = append(2., [zero_31_times])
  lunch_meal_type = append(3., [zero_31_times])
  dinner_meal_type = append(4., [zero_31_times])

  if type_of_meal == "1":
    return array([breakfast_meal_type], 'd')
  elif type_of_meal == "2":
    return array([snack_meal_type], 'd')
  elif type_of_meal == "3":
    return array([lunch_meal_type], 'd')
  elif type_of_meal == "4":
    return array([dinner_meal_type], 'd')

def form(request):
  context = {}
  context = defaultdict(lambda:"", context)
  context['plans'] = Plan.objects.all()

  if request.method == 'POST':
    form = PlanForm(request.POST)
    
    if form.is_valid():
      name = form.cleaned_data['name']
      try:
        if len(form.cleaned_data['health_labels']) == 1:
          health_labels = []
        else:
          health_labels = form.cleaned_data['health_labels']
          print('health_labels', health_labels)
          health_labels.pop()
      except KeyError:
        health_labels = []

      global nutrition_req
      global breakfast
      global snack
      global lunch
      global dinner
      nutrition_req = get_nutrition_req(form)
      breakfast = get_meals('breakfast', health_labels)
      snack = get_meals('snack', health_labels)
      lunch = get_meals('lunch', health_labels)
      dinner = get_meals('dinner', health_labels)

      if not breakfast or not snack or not lunch or not dinner:
        context['form'] = form
        context['no_plan_found'] = "No meal plan could be generated."
        return render(request, 'meals/index.html', context)
        
      # # For Basinhopping
      # meals = [breakfast, snack, lunch, snack, dinner]
      # mealplanstep = MealPlanStep()
      # x0 = generate_plan_meeting_nutrition(meals, nutrition_req)
      # plan = optimize.basinhopping(plan_cost, x0, take_step=mealplanstep, niter=3).x
      # print("Lowest cost: ", plan_cost(plan))

      # For Sim Annealing (Fortran)
        # 1 - breakfast
        # 2 - snack
        # 3 - lunch
        # 4 - dinner
      plan = select_meal_type(request.POST['meal0'])
      try:
        plan = vstack([plan, select_meal_type(request.POST['meal1'])])
      except KeyError:
        pass
      try:
        plan = vstack([plan, select_meal_type(request.POST['meal2'])])
      except KeyError:
        pass
      try:
        plan = vstack([plan, select_meal_type(request.POST['meal3'])])
      except KeyError:
        pass
      try:
        plan = vstack([plan, select_meal_type(request.POST['meal4'])])
      except KeyError:
        pass
      try:
        plan = vstack([plan, select_meal_type(request.POST['meal5'])])
      except KeyError:
        pass
      try:
        plan = vstack([plan, select_meal_type(request.POST['meal6'])])
      except KeyError:
        pass
      try:
        plan = vstack([plan, select_meal_type(request.POST['meal7'])])
      except KeyError:
        pass
      try:
        plan = vstack([plan, select_meal_type(request.POST['meal8'])])
      except KeyError:
        pass

      untouched_plan = plan
      meal_types = plan
      plan = asarray(plan, order='F')
      meal_types = asarray(meal_types, order='F')
      temperature_ini = float(request.POST['temperature_ini'])

      if not form.cleaned_data['weekly_meal_plan']:
        sim_anneal.generate_plan_meeting_nutrition(plan, nutrition_req, breakfast, snack, lunch, dinner)
        sim_anneal.sim_anneal(temperature_ini, meal_types, plan, nutrition_req, breakfast, snack, lunch, dinner)
        print ('plan[:,0]', plan[:,0])

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
          # The [::-1] reverses the array
          plan = restored_2d_plan#[::-1]

          for i, meal in enumerate(plan):
            recipe = Recipe.objects.get(id=meal[0])
            p.planrecipe_set.get_or_create(
              recipe = recipe,
              meal_number = i
            )

        return HttpResponseRedirect('/meals/plan/' + str(p.id))
      else:
        for day_num in range(0, 7):
          plan = untouched_plan
          meal_types = plan
          plan = asarray(plan, order='F')
          meal_types = asarray(meal_types, order='F')

          print("untouched_plan: ", untouched_plan)
          print("plan: ", plan)
          print("meal_types: ", meal_types)
          sim_anneal.generate_plan_meeting_nutrition(plan, nutrition_req, breakfast, snack, lunch, dinner)
          sim_anneal.sim_anneal(temperature_ini, meal_types, plan, nutrition_req, breakfast, snack, lunch, dinner)

          p, created = Plan.objects.get_or_create(
            name = "Weekly Meal Plan " + "[Day " + str((day_num + 1)) + "]: " + name,
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
            # The [::-1] reverses the array
            plan = restored_2d_plan#[::-1]

            for i, meal in enumerate(plan):
              recipe = Recipe.objects.get(id=meal[0])
              p.planrecipe_set.get_or_create(
                recipe = recipe,
                meal_number = i
              )

        return HttpResponseRedirect('/meals/weeklyplan/' + str(p.id - 6) )
  else:
    form = PlanForm()

  context['form'] = form
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

def search2(request):
  if request.method == 'POST':
    form = PlanForm(request.POST)
    if form.is_valid():
      name = form.cleaned_data['name']
      calories = form.cleaned_data['calories']

      return HttpResponseRedirect('/meals/')
  else:
    form = PlanForm()

  return render(request, 'meals/search2.html', {'form': form})

def game(request):  
  return render(request, 'meals/game.html') 