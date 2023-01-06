from django.contrib import admin
from .models import Oils, Additives, Recipes

# Register your models here.
admin.site.register(Oils)
admin.site.register(Additives)
admin.site.register(Recipes)