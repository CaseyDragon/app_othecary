from django import forms

class CreateNewRecipe(forms.Form):
    recipename = forms.CharField(max_length=100)
    superfat = forms.IntegerField()
    lyeratio = forms.DecimalField(max_digits=6, decimal_places=2)
    lyeadditives = forms.CharField(max_length=100)
    oilname1 = forms.CharField(max_length=100)
    oilamount1 = forms.DecimalField(max_digits=6, decimal_places=2)
    oilname2 = forms.CharField(max_length=100)
    oilamount2 = forms.DecimalField(max_digits=6, decimal_places=2)
    oilname3 = forms.CharField(max_length=100)
    oilamount3 = forms.DecimalField(max_digits=6, decimal_places=2)
    oilname4 = forms.CharField(max_length=100)
    oilamount4 = forms.DecimalField(max_digits=6, decimal_places=2)
    oilname5 = forms.CharField(max_length=100)
    oilamount5 = forms.DecimalField(max_digits=6, decimal_places=2)
    additive = forms.CharField(max_length=100)
