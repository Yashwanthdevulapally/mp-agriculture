from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('', include('calc.urls')),  # Ensure calc is included
]
=======
    path('', include('calc.urls')),
]
>>>>>>> 3ebd374 (Updated optimization features and added missing templates)
