from django.shortcuts import render,redirect
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import login,logout
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm

from .forms import CustomAuthenticationForm

# Create your views here.

def user_register(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('accounts:login')
    return render(request, 'accounts/register.html', context = {'form':form})




def user_login(request):
    if request.method =="POST":
        form = CustomAuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('shop:home')
    else:
    # Check if there is a message in the user's session
        if messages.get_level(request) == messages.INFO and request.GET.get('next') == reverse('shop:checkout'):
            # Delete the message from the session to prevent it from being displayed again
            messages.success(request, '')
            # Display the message to the user
            messages.info(request, 'Login is required to checkout.')
            storage = messages.get_messages(request)
            storage.used = True

        form = CustomAuthenticationForm(request)
        return render(request, 'accounts/login.html', context = {'form': form})


def user_logout(request):
        logout(request)
        return redirect('accounts:login')