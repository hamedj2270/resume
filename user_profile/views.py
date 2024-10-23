from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, get_user_model, authenticate
from user_profile.forms import LoginForm, RegisterForm



# Create your views here.


def login_page(request):
    login_form = LoginForm(request.POST or None)

    if login_form.is_valid():
        user_name = login_form.cleaned_data['username']
        password = login_form.cleaned_data['password']
        user = authenticate(request, username=user_name, password=password)
        print(user)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/')
            else:
                print("کاربری با مشخصات وارد شده یافت نشد")
        else:
            raise ValueError(request, 'نام کاربری یا رمز عبور اشتباه  است')
            return render(request, 'account/login.html')
    else:
        context = {
            'login_form': login_form,

        }

        return render(request, 'account/login.html', context)


def register_page(request):
    if request.user.is_authenticated:
        return redirect('/')
    register_form = RegisterForm(request.POST or None)

    if register_form.is_valid():
        user_name = register_form.cleaned_data.get('user_name')
        password = register_form.cleaned_data.get('password')
        email = register_form.cleaned_data.get('email')
        User.objects.create_user(username=user_name, email=email, password=password)
        return redirect('/login')

    context = {'register_form': register_form}

    return render(request, 'account/register.html', context)

