from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import logout

def register(request):

    if request.method == "POST":

        form = UserCreationForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            return redirect('home')

    else:

        form = UserCreationForm()

    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):

    form = AuthenticationForm(data=request.POST or None)

    if form.is_valid():

        login(request, form.get_user())

        return redirect('home')

    return render(request, 'accounts/login.html', {'form': form})


def profile(request):

    return render(request, 'accounts/profile.html')
def logout_view(request):
    logout(request)
    return redirect('home')
