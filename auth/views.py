import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import AuthUser


# Create your views here.
def auth(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = AuthUser(email=email, password=password)
        if user.check_client():
            request.session['token'] = 'client'
            id_client = user.check_client()
            request.session['user'] = id_client
            return HttpResponse('True')
        else:
            return HttpResponse('Такого пользователя нет')
    return render(request, 'auth/login.html', {})


def singIn(request):
    if request.method == 'POST':
        if not AuthUser.getUserByEmail(request.POST['email']):
            newUser = AuthUser()
            newUser.email = request.POST['email']
            newUser.password = request.POST['password']
            newUser.fio = request.POST['fio']
            newUser.active = 0
            newUser.last_visit = datetime.datetime.now()
            newUser.save()

            request.session['token'] = 'user'
            request.session['user'] = newUser.id

            return HttpResponse('True')
        else:
            return HttpResponse('Пользователь с таким email уже существует')
    return render(request, 'auth/registation.html', {})


def logOut(request):
    if 'user' in request.session:
        del request.session['token']
        del request.session['user']
        return redirect('auth:auth')
    else:
        return redirect('auth:auth')