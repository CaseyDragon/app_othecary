from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recipes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    recipename = models.CharField(max_length=100)
    superfat = models.IntegerField()
    lyeratio = models.DecimalField(max_digits=6, decimal_places=2)
    wateramount = models.DecimalField(max_digits=6, decimal_places=2)
    lyeamount = models.DecimalField(max_digits=6, decimal_places=2)
    lyeadditives = models.CharField(max_length=100)
    oilname1 = models.CharField(max_length=100)
    oilamount1 = models.DecimalField(max_digits=6, decimal_places=2)
    oilname2 = models.CharField(max_length=100)
    oilamount2 = models.DecimalField(max_digits=6, decimal_places=2)
    oilname3 = models.CharField(max_length=100)
    oilamount3 = models.DecimalField(max_digits=6, decimal_places=2)
    oilname4 = models.CharField(max_length=100)
    oilamount4 = models.DecimalField(max_digits=6, decimal_places=2)
    oilname5 = models.CharField(max_length=100)
    oilamount5 = models.DecimalField(max_digits=6, decimal_places=2)
    additive = models.CharField(max_length=100)
    

    def __str__(self):
        return self.name

class Oils(models.Model):
    name = models.CharField(max_length=100)
    na_sap = models.DecimalField(max_digits=5, decimal_places=4)
   
    def __str__(self):
        return self.name


class Additives(models.Model):
    name = models.CharField(max_length=100)
    suggested = models.CharField(max_length = 100)
    lyephase = models.BooleanField()

    def __str__(self):
        return self.name
