from django import forms
from django.forms import ModelForm
from .models import *


class PeliculaForm(ModelForm):

    class Meta:

     model = Pelicula
     fields = "__all__"
     widgets = {
        'name': forms.TextInput(attrs={'class':'form-control', 'pleaceholder':'pelicula'}),
        'comment': forms.Textarea(attrs={'class':'form-control'}),
        'director': forms.Select(attrs={'class':'form-control'}),
        'actores': forms.SelectMultiple(attrs={'class':'select form-control'}),
        'genero' : forms.SelectMultiple(attrs={'class' :'select form-control'}),
        'fecha_estreno' : forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        'imdb': forms.NumberInput(attrs={'class':'form-control', 'type':'number'})
    }