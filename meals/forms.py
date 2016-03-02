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
    ("Vegetarian", "Vegetarian")
  )
  health_labels = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=OPTIONS, required=False)
  weekly_meal_plan = forms.BooleanField(required=False)
  name = forms.CharField(label="Plan name:", max_length=150)
  calories = forms.FloatField(label="Calories (kcal):", min_value=1.0)
  fat = forms.FloatField(label="Fat (g):", required=False, min_value=1.0)
  carbohydrates = forms.FloatField(label="Carbohydrates (g):", required=False, min_value=1.0)
  protein = forms.FloatField(label="Protein (g):", required=False, min_value=1.0)
  sat_fat = forms.FloatField(label="Saturated Fat (g):", required=False, min_value=0.01)
  trans_fat = forms.FloatField(label="Trans Fat (g):", required=False, min_value=0.01)
  mono_unsat_fat = forms.FloatField(label="Monounsaturated Fat (g):", required=False, min_value=0.01)
  poly_unsat_fat = forms.FloatField(label="Polyunsaturated Fat (g):", required=False, min_value=0.01)
  fiber = forms.FloatField(label="Fiber (g):", required=False, min_value=0.01)
  sugar = forms.FloatField(label="Sugar (g):", required=False, min_value=0.01)
  cholesterol = forms.FloatField(label="Cholesterol (mg):", required=False, min_value=0.01)
  sodium = forms.FloatField(label="Sodium (mg):", required=False, min_value=0.01)
  calcium = forms.FloatField(label="Calcium (mg):", required=False, min_value=0.01)
  magnesium = forms.FloatField(label="Magnesium (mg):", required=False, min_value=0.01)
  potassium = forms.FloatField(label="Potassium (mg):", required=False, min_value=0.01)
  iron = forms.FloatField(label="Iron (mg):", required=False, min_value=0.01)
  zinc = forms.FloatField(label="Zinc (mg):", required=False, min_value=0.01)
  phosphorus = forms.FloatField(label="Phosphorus (mg):", required=False, min_value=0.01)
  vit_a = forms.FloatField(label="Vitamin A (IU):", required=False, min_value=0.01)
  vit_c = forms.FloatField(label="Vitamin C (mg):", required=False, min_value=0.01)
  thiamin = forms.FloatField(label="Thiamin (mg):", required=False, min_value=0.01)
  riboflavin = forms.FloatField(label="Riboflavin (mg):", required=False, min_value=0.01)
  niacin = forms.FloatField(label="Niacin (mg):", required=False, min_value=0.01)
  vit_b6 = forms.FloatField(label="Vitamin B6 (mg):", required=False, min_value=0.01)
  folic_acid = forms.FloatField(label="Folic Acid (mcg):", required=False, min_value=0.01)
  vit_b12 = forms.FloatField(label="Vitamin B12 (mcg):", required=False, min_value=0.01)
  vit_d = forms.FloatField(label="Vitamin D (IU):", required=False, min_value=0.01)
  vit_e = forms.FloatField(label="Vitamin E (IU):", required=False, min_value=0.01)
  vit_k = forms.FloatField(label="Vitamin K (mcg):", required=False, min_value=0.01)

class PopulateForm(forms.Form):
  terms = forms.CharField(
    label="Recipe terms:",
    max_length=150,
    widget=forms.TextInput(attrs={
      'class':'form-control',
      'id':'inputWarning'
    })
  )