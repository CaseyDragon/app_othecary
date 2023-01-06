from django import forms
from django.forms import ModelForm
from .models import Recipes

class CreateNewRecipe(ModelForm):
    class Meta:
        model = Recipes
        fields =('recipename', 'superfat', 'oil', 'additive')
        labels = {
            'recipename': 'Name your Recipe',
            'superfat': 'Choose your superfat percent',
            'oil': 'Pick Your Oil',
            'additive': 'Choose an Extra'

        }
        widgets = {
            'recipename': forms.TextInput(attrs={'class': 'control pb-2 mb-4'}),
            'superfat': forms.TextInput(attrs={'class': 'control pb-2 mb-4'}),
            'oil': forms.Select(attrs={'class': ' my-3'}),
            'additive': forms.Select(attrs={'class': ' my-3'}),
        }


    # recipename = forms.CharField(max_length=100)
    # superfat = forms.IntegerField()
    # lyeratio = forms.DecimalField(max_digits=6, decimal_places=2)
    # lyeadditives = forms.CharField(max_length=100)
    # oilname1 = forms.ManyToManyField(Oils, max_length=100)
    # oilamount1 = forms.DecimalField(max_digits=6, decimal_places=2)
    # oilname2 = forms.CharField(max_length=100)
    # oilamount2 = forms.DecimalField(max_digits=6, decimal_places=2)
    # oilname3 = forms.CharField(max_length=100)
    # oilamount3 = forms.DecimalField(max_digits=6, decimal_places=2)
    # oilname4 = forms.CharField(max_length=100)
    # oilamount4 = forms.DecimalField(max_digits=6, decimal_places=2)
    # oilname5 = forms.CharField(max_length=100)
    # oilamount5 = forms.DecimalField(max_digits=6, decimal_places=2)
    # additive = forms.CharField(max_length=100)
