from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .forms import SignUpForm

# Create your views here.
@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html')

@login_required
def edit(request):
    return render(request, 'account/edit.html')

def register(request):
    
    # Blocked registration for logged in
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            form = SignUpForm(request.POST)

            if form.is_valid():
                form.save()
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect('index')
        else:
            form = SignUpForm(initial={'gender': False})
    
    context = { 'form': form }
    return render(request, 'registration/register.html', context)
