from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Oils, Additives, Recipes
from .forms import CreateNewRecipe

def home(response):
    return render(response, 'recipemaker/home.html', {})

def create(response):
    if response.method == 'POST':
        form = CreateNewRecipe(response.POST)
        if form.is_valid():
            n=form.cleaned_data["recipename"]
            rec = Recipes(name=n)
            rec.save()

        return HttpResponseRedirect('/%i' %rec.id)
    else:
        form = CreateNewRecipe()
    return render(response, 'recipemaker/create.html', {"form":form})
# @login_required(login_url='/registration/login')
# def create(request):
#     form = CreateNewRecipe()
#     if request.method == 'POST':
#         form = CreateNewRecipe(request.POST)
#         if form.is_valid():
#             # Recipes.user.objects.create(**form.cleaned_data)
#             n = form.cleaned_data["recipename"]
#             recipe = Recipes(name=n)
#             # recipe.save()
#             # request.user.recipes.create(recipe)
#         return HttpResponseRedirect('/%i' %recipe.id)
#     else:    
#         form = CreateNewRecipe()
#     return render(request, 'recipemaker/create.html', {'form':form})

def oils_list(request):
    oils = Oils.objects.all()
    return render(request, 'recipemaker/oils_list.html', {'oils': oils})

def oils_detail(request, id):
    oil = Oils.objects.get(id=id)
    return render(request, 'recipemaker/oils_detail.html', {'oil': oil})

def additives_list(request):
    additives= Additives.objects.all()
    return render(request, 'recipemaker/additives_list.html', {'additives': additives})

def additives_detail(request, id):
    additive = Additives.objects.get(id=id)
    return render(request, 'recipemaker/additives_detail.html', {'additive': additive})

@login_required(login_url='/registration/login')
def my_recipes(response):
    recipes = Recipes.objects.all()
        # if recipe in response.user.recipes.all():
    return render(response, 'recipemaker/my_recipes.html', {'recipes': recipes})

    

@login_required(login_url='/registration/login')
def recipe_detail(response, id):
    recipe = Recipes.objects.get(id=id)
   
    # work out code for scaling here I believe
    # if response.POST.get('save'):

    # elif response.POST.get('scaleIt'):
    #     pass    
    return render(response, 'recipemaker/recipe_detail.html', {'recipe': recipe})

def volume_calc(response):
    return render(response, 'recipemaker/volume_calc.html', {})

def basic_formulations(response):
    return render(response, 'recipemaker/basic_formulations.html', {})