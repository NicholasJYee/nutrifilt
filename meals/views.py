from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
  context = {
    'first_name': "Hatim"
  }
  return HttpResponse("Hello")
  # return(request, 'meals/index.html', context)