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
  health_labels = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=OPTIONS)
  name = forms.CharField(label="Plan name:", max_length=150)
  calories = forms.FloatField(label="Calories (kcal):")
  fat = forms.FloatField(label="Fat (g):", required=False)
  carbohydrates = forms.FloatField(label="Carbohydrates (g):", required=False)
  protein = forms.FloatField(label="Protein (g):", required=False)
  sat_fat = forms.FloatField(label="Saturated Fat (g):", required=False)
  trans_fat = forms.FloatField(label="Trans Fat (g):", required=False)
  mono_unsat_fat = forms.FloatField(label="Monounsaturated Fat (g):", required=False)
  poly_unsat_fat = forms.FloatField(label="Polyunsaturated Fat (g):", required=False)
  fiber = forms.FloatField(label="Fiber (g):", required=False)
  sugar = forms.FloatField(label="Sugar (g):", required=False)
  cholesterol = forms.FloatField(label="Cholesterol (mg):", required=False)
  sodium = forms.FloatField(label="Sodium (mg):", required=False)
  calcium = forms.FloatField(label="Calcium (mg):", required=False)
  magnesium = forms.FloatField(label="Magnesium (mg):", required=False)
  potassium = forms.FloatField(label="Potassium (mg):", required=False)
  iron = forms.FloatField(label="Iron (mg):", required=False)
  zinc = forms.FloatField(label="Zinc (mg):", required=False)
  phosphorus = forms.FloatField(label="Phosphorus (mg):", required=False)
  vit_a = forms.FloatField(label="Vitamin A (micro g):", required=False)
  vit_c = forms.FloatField(label="Vitamin C (mg):", required=False)
  thiamin = forms.FloatField(label="Thiamin (mg):", required=False)
  riboflavin = forms.FloatField(label="Riboflavin (mg):", required=False)
  niacin = forms.FloatField(label="Niacin (mg):", required=False)
  vit_b6 = forms.FloatField(label="Vitamin B6 (mg):", required=False)
  folic_acid = forms.FloatField(label="Folic Acid (micro g):", required=False)
  vit_b12 = forms.FloatField(label="Vitamin B12 (micro g):", required=False)
  vit_d = forms.FloatField(label="Vitamin D (micro g):", required=False)
  vit_e = forms.FloatField(label="Vitamin E (mg):", required=False)
  vit_k = forms.FloatField(label="Vitamin K (micro g):", required=False)

class PopulateForm(forms.Form):
  terms = forms.CharField(
    label="Recipe terms:",
    max_length=150,
    widget=forms.TextInput(attrs={
      'class':'form-control',
      'id':'inputWarning'
    })
  )