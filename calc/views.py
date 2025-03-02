from django.shortcuts import render

def home(request):
    return render(request, 'calc/home.html')

def optimization(request):
    return render(request, 'calc/optimization.html')
