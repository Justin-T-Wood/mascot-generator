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
	animal =  form.cleaned_data.get('desired_animal')
	if animal == "Cat":
		image = "cat_collage.jpg"
	if animal == "Turtle":
		image = "turtle_collage.jpg"
	if animal == "Dragon":
		image = "dragon_collage.jpg"
	if animal == "Octopus":
		image = "octopus_collage.jpg"
	else:
		image = ""
        return render(request,'mga/generated.html', {'image': image})
    else:
        form = GeneratorForm()
        return render(request, 'mga/generator.html', {'form': form })
