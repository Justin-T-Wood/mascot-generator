from django.shortcuts import render, redirect
from django.template import loader
from mascotGeneratorApp.forms import GeneratorForm

def about(request):
    return render(request, 'mga/about.html')

def contact(request):
    return render(request, 'mga/contact.html')


def home(request):
    return render(request, 'mga/home.html')

def generated(request):
    return render(request, 'mga/generated.html')

def generator(request):
    form = GeneratorForm(request.POST)
    if form.is_valid():
        image = "home5.jpeg"
        return render(request,'mga/generated.html', {'image': image})
    else:
        form = GeneratorForm()
        return render(request, 'mga/generator.html', {'form': form })
