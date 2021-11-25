from django.http import HttpResponse
from django.shortcuts import redirect, render

from core.models import UserExtSettings
from tracker.forms import SettingsExtForm
from tracker.models import UserRepository


def settingsExt(request):
    if 'user' in request.session:
        userExt = UserRepository.objects.get(pk=request.session['user']).userextsettings_set.all().order_by('-date_created')

        return render(request, 'tracker/settingsExt.html', {'user_extend': userExt})
    else:
        return redirect('auth:auth')


def settingsExtCreate(request):
    if 'user' in request.session:
        if request.method == 'POST':
            settingsExtForm = SettingsExtForm(request.POST)
            if settingsExtForm.is_valid():
                settingsExtForm.instance.user = UserRepository.objects.get(pk=request.session['user'])
                settingsExtForm.save()
                return HttpResponse('True')
            else:
                return HttpResponse(settingsExtForm.errors.as_json())
        formExt = SettingsExtForm()
        return render(request, 'tracker/settingsExtCreate.html', {'formExt': formExt})
    else:
        return redirect('auth:auth')


def settingsExtEdit(request, id):
    if 'user' in request.session:
        userExt = UserExtSettings.objects.get(pk=id)
        settingsExtForm = SettingsExtForm(instance=userExt)
        if request.method == 'POST':
            settingsExtForm = SettingsExtForm(request.POST, instance=userExt)
            if settingsExtForm.is_valid():
                settingsExtForm.save()
                return HttpResponse('True')
            else:
                return HttpResponse(settingsExtForm.errors.as_json())
        return render(request, 'tracker/settingsExtEdit.html', {'formExt': settingsExtForm})
    else:
        return redirect('auth:auth')


def settingsExtDelete(request, id):
    if 'user' in request.session:
        userExt = UserExtSettings.objects.get(pk=id)
        if userExt:
            userExt.delete()
        return redirect('tracker:settingsExt')
    else:
        return redirect('auth:auth')