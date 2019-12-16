from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.urls import reverse_lazy
from django.utils.deprecation import MiddlewareMixin
from django.views.generic import TemplateView


from .forms import UserUpdateForm, ProfileUpdateForm


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

        if len(password1) == 0:
            messages.info(request, 'Password is required')
            return redirect('/register')
        elif len(password1) < 3:
            messages.info(request, 'Password is too short. It must have at least 3 characters')
            return redirect('/register')
        elif len(username) == 0:
            messages.info(request, 'Username is required')
            return redirect('/register')
        elif len(username) < 3:
            messages.info(request, 'Username is too short. It must have at least 3 characters')
            return redirect('/register')
        else:
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


@login_required
def profile(request):
    return render(request, 'profile.html')


class ProfileUpdate(MiddlewareMixin, TemplateView):
    user_form = UserUpdateForm
    profile_form = ProfileUpdateForm
    template_name = 'profile-update.html'

    def post(self, request):
        post_data = request.POST or None
        file_data = request.FILES or None


        if request.method == "POST":
            user_form = UserUpdateForm(post_data, instance=request.user)
            profile_form = ProfileUpdateForm(post_data, file_data, instance=request.user.profile)

            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
                messages.info(request, 'Your profile was successfully updated!')
                return HttpResponseRedirect(reverse_lazy('profile'))
        else:
            user_form = UserUpdateForm(instance=request.user)
            profile_form = ProfileUpdateForm(instance=request.user.profile)

        context = {
            'user_form': user_form,
            'profile_form': profile_form
        }

        # return render(request, 'profile.html', context)
        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
