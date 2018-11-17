from django import forms

class GeneratorForm(forms.Form):
    CHOICES = (('Cat', 'Cat'),('Dragon', 'Dragon'),('Turtle','Turtle'),('Octopus','Octopus'))
    what_is_your_name = forms.CharField(max_length=100)(required=false)
    what_is_your_quest = forms.CharField(max_length=100)
    what_is_the_air_speed_velocity_of_an_unladen_swallow = forms.CharField(max_length=100)
    desired_animal = forms.ChoiceField(choices=CHOICES)
    
