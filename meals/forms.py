from django import forms

class PlanForm(forms.Form):
  name = forms.CharField(label="Plan name:", max_length=150)
  calories = forms.FloatField(label="Calories:")