from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from tracker.forms import MainSettingForm, PasswordSettingForm
from tracker.models import UserRepository


def dashboard(request):
    if 'user' in request.session:
        return render(request, 'base/dashboard-content.html', {})
    else:
        return redirect('auth:auth')


def settings(request):
    if 'user' in request.session:
        user = UserRepository.objects.get(pk=request.session['user'])
        formMain = MainSettingForm({
            'fio': user.fio,
            'email': user.email
        }, user=user)
        formPass = PasswordSettingForm()
        if request.method == 'POST':
            mainSettingForm = MainSettingForm(request.POST, user=user)
            if mainSettingForm.is_valid():
                user.fio = mainSettingForm.cleaned_data['fio']
                user.email = mainSettingForm.cleaned_data['email']
                user.save()
                return HttpResponse('True')
            else:
                print(mainSettingForm.errors.as_json())
                return HttpResponse(mainSettingForm.errors.as_json())
        return render(request, 'tracker/settings.html', {'formMain': formMain, 'formPass': formPass})
    else:
        return redirect('auth:auth')


def settingsext(request):
    if 'user' in request.session:
        user = UserRepository.objects.get(pk=request.session['user'])
        formMain = MainSettingForm({
            'fio': user.fio,
            'email': user.email
        }, user=user)
        formPass = PasswordSettingForm()
        if request.method == 'POST':
            mainSettingForm = MainSettingForm(request.POST, user=user)
            if mainSettingForm.is_valid():
                user.fio = mainSettingForm.cleaned_data['fio']
                user.email = mainSettingForm.cleaned_data['email']
                user.save()
                return HttpResponse('True')
            else:
                print(mainSettingForm.errors.as_json())
                return HttpResponse(mainSettingForm.errors.as_json())
        return render(request, 'tracker/settings.html', {'formMain': formMain, 'formPass': formPass})
    else:
        return redirect('auth:auth')
