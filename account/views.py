from django.contrib.auth import login ,logout
from django.shortcuts import redirect, render
from .forms import LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home:contact-us')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home:contact-us')
            else:
                form.add_error(None, "username or password is incorrect")
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home:contact-us')
