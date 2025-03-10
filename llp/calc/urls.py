from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('', home, name='home'),
    path('optimize/', optimization, name='optimization'),
=======
    path('', views.home, name='home'),
    path('optimization/', views.optimization, name='optimization'),
    path('graphical-method/', views.graphical_method, name='graphical_method'),
    path('simplex-method/', views.simplex_method, name='simplex_method'),
    path('transportation-method/', views.transportation_method, name='transportation_method'),
    path('knapsack-method/', views.knapsack_method, name='knapsack_method'),
>>>>>>> 3ebd374 (Updated optimization features and added missing templates)
]
