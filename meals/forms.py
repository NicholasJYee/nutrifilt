from django import forms

class PlanForm(forms.Form):
  OPTIONS = (
    ("Dairy-Free", "Dairy-Free"),
    ("Egg-Free", "Egg-Free"),
    ("Fish-Free", "Fish-Free"),
    ("Gluten-Free", "Gluten-Free"),
    ("Low Sugar", "Low Sugar"),
    ("Paleo", "Paleo"),
    ("Peanut-Free", "Peanut-Free"),
    ("Shellfish-Free", "Shellfish-Free"),
    ("Soy-Free", "Soy-Free"),
    ("Tree-Nut-Free", "Tree-Nut-Free"),
    ("Vegan", "Vegan"),
    ("Vegetarian", "Vegetarian"),
    ("None", "None")
  )
  health_labels = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=OPTIONS, required=False)
  weekly_meal_plan = forms.BooleanField(required=False)
  name = forms.CharField(label="Plan name:", max_length=150)
  calories = forms.FloatField(label="Calories (kcal):", min_value=1.0)
  fat = forms.FloatField(label="Fat (g):", required=False, min_value=1.0)
  carbohydrates = forms.FloatField(label="Carbohydrates (g):", required=False, min_value=1.0)
  protein = forms.FloatField(label="Protein (g):", required=False, min_value=1.0)
  sat_fat = forms.FloatField(label="Saturated Fat (g):", required=False, min_value=1.0)
  trans_fat = forms.FloatField(label="Trans Fat (g):", required=False, min_value=1.0)
  mono_unsat_fat = forms.FloatField(label="Monounsaturated Fat (g):", required=False, min_value=1.0)
  poly_unsat_fat = forms.FloatField(label="Polyunsaturated Fat (g):", required=False, min_value=1.0)
  fiber = forms.FloatField(label="Fiber (g):", required=False, min_value=1.0)
  sugar = forms.FloatField(label="Sugar (g):", required=False, min_value=1.0)
  cholesterol = forms.FloatField(label="Cholesterol (mg):", required=False, min_value=1.0)
  sodium = forms.FloatField(label="Sodium (mg):", required=False, min_value=1.0)
  calcium = forms.FloatField(label="Calcium (mg):", required=False, min_value=1.0)
  magnesium = forms.FloatField(label="Magnesium (mg):", required=False, min_value=1.0)
  potassium = forms.FloatField(label="Potassium (mg):", required=False, min_value=1.0)
  iron = forms.FloatField(label="Iron (mg):", required=False, min_value=1.0)
  zinc = forms.FloatField(label="Zinc (mg):", required=False, min_value=1.0)
  phosphorus = forms.FloatField(label="Phosphorus (mg):", required=False, min_value=1.0)
  vit_a = forms.FloatField(label="Vitamin A (micro g):", required=False, min_value=1.0)
  vit_c = forms.FloatField(label="Vitamin C (mg):", required=False, min_value=1.0)
  thiamin = forms.FloatField(label="Thiamin (mg):", required=False, min_value=1.0)
  riboflavin = forms.FloatField(label="Riboflavin (mg):", required=False, min_value=1.0)
  niacin = forms.FloatField(label="Niacin (mg):", required=False, min_value=1.0)
  vit_b6 = forms.FloatField(label="Vitamin B6 (mg):", required=False, min_value=1.0)
  folic_acid = forms.FloatField(label="Folic Acid (micro g):", required=False, min_value=1.0)
  vit_b12 = forms.FloatField(label="Vitamin B12 (micro g):", required=False, min_value=1.0)
  vit_d = forms.FloatField(label="Vitamin D (micro g):", required=False, min_value=1.0)
  vit_e = forms.FloatField(label="Vitamin E (mg):", required=False, min_value=1.0)
  vit_k = forms.FloatField(label="Vitamin K (micro g):", required=False, min_value=1.0)

class PopulateForm(forms.Form):
  terms = forms.CharField(
    label="Recipe terms:",
    max_length=150,
    widget=forms.TextInput(attrs={
      'class':'form-control',
      'id':'inputWarning'
    })
  )