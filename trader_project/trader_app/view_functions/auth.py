from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required

from ..models import Trader
from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.http import HttpResponseNotFound


def login(request):
    if request.user.is_authenticated:
        return HttpResponseNotFound('<h1>You need to log out first</h1>')
    if request.method == 'POST':
        trader_name = request.POST.get('username').lower()
        password = request.POST.get('password')
        print(trader_name, password)
        if not trader_name or not password:
            messages.error(request, 'Please fill in all fields')
            return render(request, 'login.html')
        try:
            trader = Trader.objects.filter(name=trader_name).first()
            # print(trader.name)
            if not trader:
                messages.error(request, 'Invalid username')
                return render(request, 'login.html')
            user = authenticate(request, username=trader.name.lower(), password=password)
            if user is not None:
                if user.is_superuser:
                    auth_login(request, user)
                    url = reverse('admin_dashboard')
                    return redirect(url)
                else:
                    auth_login(request, user)
                    url = reverse('user_dashboard', args=[trader.id])
                    return redirect(url)
            else:
                messages.error(request, 'Invalid username or password')
                return render(request, 'login.html')
        except Trader.DoesNotExist:
            messages.error(request, 'Invalid username')
            return render(request, 'login.html')
    return render(request, 'login.html')


@login_required(login_url='login')
def logout(request):
    if not request.user.is_authenticated:
        messages.error(request, 'You need to be logged-in')
        return redirect('login')
    auth.logout(request)
    return redirect('login')
