from django import forms
from django.forms import ModelForm
from .models import *

class ProductoForm(ModelForm):

    class Meta:

     model = Productos
     fields = "__all__"
     widgets = {
        'id': forms.NumberInput(attrs={'class':'form-control', 'type':'number'}),
        'name': forms.TextInput(attrs={'class':'form-control'}),
        'cantidad': forms.NumberInput(attrs={'class':'form-control', 'type':'number'}),
        'lote': forms.NumberInput(attrs={'class':'form-control','type':'number' }),
        'stock': forms.TextInput(attrs={'class':'form-control', 'pleaceholder' : 'stock'}),
        'precio': forms.NumberInput(attrs={'class':'form-control', 'type':'number'}),
        'fecha': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
        'marca': forms.TextInput(attrs={'class':'form-control', 'pleaceholder': 'marca'})
    }