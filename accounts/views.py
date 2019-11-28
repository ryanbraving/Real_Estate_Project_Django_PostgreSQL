from django.shortcuts import render, redirect
from django.contrib import messages, auth
# from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

# Create your views here.


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password != password2:
            messages.error(request, 'passwords do not match!')
            return redirect('register')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'This username is taken')
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'This email is being used')
            return redirect('register')
        else:
            user = User.objects.create_user(
                first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            # straight login after register
            # alth.login(request, user)
            # messages.success(request, 'You are now logged in')
            # return redirect('index')
            user.save()
            messages.success(request, 'you are now registered please log in')
            return redirect('login')

    return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        # login user
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, "you are now logged in")
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials!')
            return redirect('login')

    return render(request, 'accounts/login.html')


def logout(request):
    auth.logout(request)
    messages.success(request, 'You are now logged out')
    return redirect('index')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
