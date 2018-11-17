from django.shortcuts import render
from django.template import loader

def about(request):
    return render(request, 'mga/about.html')
    
def home(request):
    return render(request, 'mga/home.html')

def generator(request):
    return render(request, 'mga/generator.html')
