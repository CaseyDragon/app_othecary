from django.shortcuts import render, redirect
from .forms import SignUpForm

# Create your views here.


def sign_up(response):
    if response.method == 'POST':
        form = SignUpForm(response.POST)
        if form.is_valid():
            form.save()
            # user = form.save()
            # login(response, user)
            return redirect('/recipemaker/home')
    else:
        form = SignUpForm()
    
    return render(response, 'accounts/signup.html', {'form': form})
