from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .forms import SignUpForm
from .models import ExtendedUser

# Create your views here.
@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html')

@login_required
def edit(request):
    try:
        query = ExtendedUser.objects.get(id=request.user.id)
    except ExtendedUser.DoesNotExist:
        raise Http404("User does not exist")

    if request.method == 'POST':
        print('POSTED')

    return render(request, 'account/edit.html', {'content': query})

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
