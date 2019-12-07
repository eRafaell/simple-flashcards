from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth


def main_page_view(request):
    return render(request, "main_page.html")


def register(request):
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('/register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email taken')
                return redirect('/register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email,
                                                first_name=first_name, last_name=last_name)
                user.save()
                messages.info(request, f'User {username} created')
                return redirect('/')
        else:
            messages.info(request, 'Password not matching')
            return redirect('/register')

    else:
        return render(request, "register.html")


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.info(request, f'User {username} logged in')
            return redirect('/')
        else:
            messages.info(request, 'Invalid username or password')
            return redirect('/login')
    else:
        return render(request, "login.html")


def logout(request):
    username = request.user.username
    auth.logout(request)
    messages.success(request, f"{username} has just logged out")
    return redirect('/')
