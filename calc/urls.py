from django.urls import path
from .views import home, optimization

urlpatterns = [
    path('', home, name='home'),
    path('optimization/', optimization, name='optimization'),
]
