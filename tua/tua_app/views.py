from django.shortcuts import render, redirect
from .models import Category, Job, plan, deli, vak
from django.contrib.auth import authenticate, logout
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.contrib.auth import login as django_login



def main(request):
    categories = Category.objects.all()
    jobs = Job.objects.all()
    plans = plan.objects.all()
    context = {
        'categories': categories,
        'jobs': jobs,
        'plans': plans
    }
    return render(request, "./main.html", context)
def valu(request):
    categories = Category.objects.all()
    plans = plan.objects.all()
    context = {
        'categories': categories,
        'plans': plans
    }
    return render(request, "./tri.html", context)
def stand(request):
    categories = Category.objects.all()
    jobs = Job.objects.all()

    context = {
        'categories': categories,
        'jobs': jobs
    }
    return render(request, "./second.html", context)
def deliv(request):
    categories = Category.objects.all()
    delis = deli.objects.all()
    context = {
        'categories': categories,
        'delis': delis
    }
    return render(request, "./four.html", context)
def job(request):
    categories = Category.objects.all()
    vaks = vak.objects.all()

    context = {
        'categories': categories,
        'vaks': vaks
    }
    return render(request, "./seven.html", context)
def disa(request):
    categories = Category.objects.all()
    jobs = Job.objects.all()

    context = {
        'categories': categories,
        'jobs': jobs
    }
    return render(request, "./six.html")
def cal(request):
    categories = Category.objects.all()
    jobs = Job.objects.all()

    context = {
        'categories': categories,
        'jobs': jobs
    }
    return render(request, "./five.html")
def good(request):
    categories = Category.objects.all()
    jobs = Job.objects.all()

    context = {
        'categories': categories,
        'jobs': jobs
    }
    return render(request, "./eight.html")
def login(request):
    return render(request, "./nine.html")
def reg(request):
    return render(request, "./on.html")
def logout_view(request):


    
    logout(request)
    return redirect('home')
def sign_up(request):
    return render(request, 'sign-up.html')
def login_up(request):
    return render(request, 'login.html')


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Сохранение данных и редирект на другую страницу
            user=form.save()
            return redirect('home')  # После успешной регистрации редиректим на главную страницу
    else:
        form = SignUpForm()

    return render(request, 'sign-up.html', {'form': form})

from django.contrib.auth import authenticate, login as django_login

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import messages  # Импортируем модуль для вывода сообщений

def login_page(request):
    # Если пользователь уже авторизован, перенаправляем на домашнюю страницу
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        # Создаем форму аутентификации с данными из запроса
        form = AuthenticationForm(request, data=request.POST)
        
        # Проверка, прошла ли форма валидацию
        if form.is_valid():
            # Получаем имя пользователя и пароль из формы
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            # Аутентификация пользователя
            user = authenticate(username=username, password=password)
            
            # Если пользователь найден, авторизуем его
            if user is not None:
                login(request, user)
                return redirect('home')  # Перенаправляем на домашнюю страницу
            else:
                # Если пользователь не найден, выводим сообщение об ошибке
                messages.error(request, "Неверное имя пользователя или пароль.")
        else:
            # Если форма не прошла валидацию, выводим сообщение об ошибке
            messages.error(request, "Пожалуйста, исправьте ошибки в форме.")
    else:
        # Создаем пустую форму при GET-запросе
        form = AuthenticationForm()

    # Передаем форму в шаблон
    context = {
        'form': form
    }
    return render(request, 'login.html', context)



def logout_action(request):
    logout(request)
    return redirect('home')