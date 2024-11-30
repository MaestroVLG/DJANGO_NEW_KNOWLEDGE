from django.shortcuts import render
from .forms import UserRegister
from .models import Game

users = ['user1', 'user2', 'user3']


def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            # Проверка на существование пользователя
            if Buyer.objects.filter(name=username).exists():
                info['error'] = 'Пользователь уже существует'
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            else:
                # Добавление пользователя в базу данных
                Buyer.objects.create(name=username)
                return render(request, 'fifth_task/registration_page.html', {'message': f'Приветствуем, {username}!'})
    else:
        form = UserRegister()

    info['form'] = form
    return render(request, 'fifth_task/registration_page.html', info)

# Главная страница
def home_view(request):
    return render(request, 'fourth_task/home.html')

# Страница магазина
#def store_view(request):
#   games = ["Atomic Heart", "Cyberpunk 2077"]
#    return render(request, 'fourth_task/store.html', {'games': games})

def store_view(request):
    games = Game.objects.all()
    return render(request, 'fourth_task/store.html', {'games': games})

# Страница корзины
def cart_view(request):
    return render(request, 'fourth_task/cart.html')




