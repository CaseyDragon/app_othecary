from django.db import models
from django.contrib.auth.models import User

# Create your models here.
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

class Recipes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    recipename = models.CharField(max_length=100)
    superfat = models.IntegerField()
    lyeratio = models.DecimalField(max_digits=6, decimal_places=2, default=0.33)
    oil = models.ManyToManyField(Oils, blank=True)
    additive = models.ManyToManyField(Additives, blank=True)
    

    def __str__(self):
        return self.name


