from django import forms

class PopulateForm(forms.Form):
  terms = forms.CharField(label="Search terms:", max_length=150)
  