from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save() # saves the form data to Django inbuilt Users model.
            username = form.cleaned_data.get('username')
            messages.success(request, f' Your Account created, you are redirected to Login!')
            return redirect('login')
        else:
            messages.warning(request, f'Account is not created, please follow all password rules!')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')