from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Oils, Additives, Recipes
from .forms import CreateNewRecipe

def home(response):
    return render(response, 'recipemaker/home.html', {})

def create(request):
    # submitted = False
    if request.method == 'POST':
        form = CreateNewRecipe(request.POST)
        if form.is_valid():
            recipe = form.save()
            return redirect('recipe_list', id=recipe.id)
            # return HttpResponseRedirect('/create?submitted=True')
            # n=form.cleaned_data["recipename"]
            # recipe = Recipes(n)
            # recipe.save()
            # response.user.recipes.create(recipe)
    else:
        form = CreateNewRecipe
        #  
    return render(request, 'recipemaker/create.html', {"form":form})

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
    return render(response, 'recipemaker/recipe_detail.html', {'recipe': recipe})

def volume_calc(response):
    return render(response, 'recipemaker/volume_calc.html', {})

def basic_formulations(response):
    return render(response, 'recipemaker/basic_formulations.html', {})