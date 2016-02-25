from django.conf.urls import url
from . import views

urlpatterns = [
  # Nick's test page
  url(r'^form/', views.form, name='form'),
  url(r'^populate/', views.populate, name='populate'),
  url(r'^plan/search/$', views.searchplan, name = 'name'),
  url(r'^plan/(?P<plan_id>\w+)/', views.plan, name='plan'),


  # App homepage
  url(r'^$', views.index, name='index'),

  #For the search form
  url(r'^search/$', views.search, name='search'),

]