import django
from django import forms
from django.shortcuts import render, redirect
from .models import Buyer




class UserRegister(forms.Form):
    username = forms.CharField(max_length=30, label="Введите логин")
    password = forms.CharField(min_length=8, widget=forms.PasswordInput, label="Введите пароль")
    repeat_password = forms.CharField(min_length=8, widget=forms.PasswordInput, label="Повторите пароль")
    age = forms.IntegerField(max_value=999, label="Введите свой возраст")



def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            balance = form.cleaned_data['balance']
            age = form.cleaned_data['age']

            exists = Buyer.objects.filter(name=name).exists()
            if not exists:
                Buyer.objects.create(name=name, balance=balance, age=age)
                return redirect('home')

    else:
        form = RegisterForm()

    context = {
        'form': form,
    }
    return render(request, 'fifth_task/register.html', context)

def store_view(request):
    games = Game.objects.all()

    context = {
        'games': games,
    }
    return render(request, 'fourth_task/store.html', context)
