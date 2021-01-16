from django.shortcuts import render

# Create your views here.

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from clinic.forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.clinic.clinic_name = form.cleaned_data.get('clinic_name')
            user.clinic.address = form.cleaned_data.get('address')
            user.clinic.phone_number = form.cleaned_data.get('phone_number')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('/ ')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})