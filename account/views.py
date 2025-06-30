from django.contrib.auth import login, logout
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


def register_view(request):
    context = {'error': []}

    if request.user.is_authenticated:
        return redirect('home:contact-us')

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            context['error'].append('passwords do not match')
            return render(request, 'account/login.html', context)

        if User.objects.filter(username=username).exists():
            context['error'].append('name already exists')
            return render(request, 'account/login.html', context)
        if User.objects.filter(email=email).exists():
            context['error'].append("email already exists")
            return render(request, 'account/login.html', context)

        user = User.objects.create_user(username=username, email=email, password=password1)

        user = authenticate(request, username=username, password=password1)
        if user is not None:
            login(request, user)
            return redirect('home:contact-us')
        else:
            context['error'].append("email or password is incorrect")
            return render(request, 'account/login.html', context)

    return render(request, 'account/login.html')
