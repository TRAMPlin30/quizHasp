from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from accounts.forms import UserLoginForm, UserRegistrationForm


def login_view(request):
    form_login = UserLoginForm(request.POST or None)
    _next = request.GET.get('next')
    if form_login.is_valid():
        username = form_login.cleaned_data.get('username')
        password = form_login.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        _next = _next or '/'
        return redirect(_next)
    return render(request, 'accounts/login.html', {'form': form_login})


def logoute_view(request):
    logout(request)
    return redirect('/')


def home_view(request):
    name = 'Главная страница сайта'
    return render(request, 'accounts/home.html', {'name': name})


def user_registration_view(request):
    if request.method == 'POST':
        form_register = UserRegistrationForm(request.POST)
        if form_register.is_valid():
            new_user = form_register.save(commit=False)
            new_user.set_password(form_register.cleaned_data['password'])
            new_user.save()
            return render(request, 'accounts/register_done.html', {'new_user': new_user})

        return render(request, 'accounts/register.html', {'form_register': form_register})

    else:
        form_register = UserRegistrationForm()
        context = {'form_register': form_register}
        return render(request, 'accounts/register.html', context)


def dashboard(request):
    if request.user.is_authenticated:
        name = 'Личный кабинет'
        return render(request, 'accounts/dashboard.html', {'name': name})
    else:
        form_register = UserRegistrationForm()
        context = {'form_register': form_register}
        return render(request, 'accounts/register.html', context)
