from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.decorators import login_required

from .utils import passVerify
from .forms import SignUpForm
from .models import ExtendedUser

# Create your views here.
@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html')

@login_required
def edit(request):
    try:
        user = ExtendedUser.objects.get(id=request.user.id)
    except ExtendedUser.DoesNotExist:
        raise Http404("User does not exist")

    if request.method == 'POST':
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.url = request.POST['url']
        user.biography = request.POST['biography']
        user.email = request.POST['email']

        # Verify old password
        if(user.check_password(request.POST['old_password'])):

            # Check if password are the same / validate
            if(passVerify(request)):

                # Change password
                user.set_password(request.POST['new_password1'])
                update_session_auth_hash(request, user)
            
            else:
                print('password diffrent or fields blank!')

        else:
            print('error')
        user.save()

    return render(request, 'account/edit.html', {'content': user})

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
