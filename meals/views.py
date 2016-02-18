from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
  context = {
    'first_name': "Hatim"
  }
  return render(request, 'meals/index.html', context)