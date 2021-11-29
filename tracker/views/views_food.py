import datetime
import json

from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import render, redirect

from core.models import UserFood
from tracker.forms import FoodForm
from tracker.models import UserRepository

from django.db.models import F
from django.utils.safestring import SafeString


def foodIndex(request):
    if 'user' in request.session:
        list_food = UserFood.objects.filter(user_id=request.session['user']).all()
        countAll = UserFood.objects.filter(user_id=request.session['user'], date_created__day=datetime.date.today().day).aggregate(Sum('cal'))
        return render(request, 'food/index.html', {'list_food': list_food, 'today': datetime.date.today(), 'countAll': countAll})
    else:
        return redirect('auth:auth')


def foodAdd(request):
    if 'user' in request.session:
        if request.method == 'POST':
            settingsExtForm = FoodForm(request.POST)
            if settingsExtForm.is_valid():
                settingsExtForm.instance.user = UserRepository.objects.get(pk=request.session['user'])
                settingsExtForm.save()
                return redirect('tracker:foodIndex')
            else:
                return HttpResponse(settingsExtForm.errors.as_json())
        formFood = FoodForm()
        return render(request, 'food/add.html', {'formFood': formFood})
    else:
        return redirect('auth:auth')


def foodUpdate(request, id):
    if 'user' in request.session:
        userExt = UserFood.objects.get(pk=id)
        settingsExtForm = FoodForm(instance=userExt)
        if request.method == 'POST':
            settingsExtForm = FoodForm(request.POST, instance=userExt)
            if settingsExtForm.is_valid():
                settingsExtForm.save()
                return redirect('tracker:foodIndex')
            else:
                return HttpResponse(settingsExtForm.errors.as_json())
        return render(request, 'food/update.html', {'formFood': settingsExtForm})
    else:
        return redirect('auth:auth')


def foodDelete(request, id):
    if 'user' in request.session:
        obj = UserFood.objects.get(pk=id)
        obj.delete()
        return redirect('tracker:foodIndex')
    else:
        return redirect('auth:auth')


def foodStat(request):
    data = []
    dataObj = UserFood.objects.filter(user_id=request.session['user']).values(date=F('date_created__date')).order_by('date_created__date').annotate(cal=Sum('cal'))

    for item in dataObj:
        data.append({
            'date': str(item['date']),
            'cal': item['cal'],
        })

    data = json.dumps(list(data))
    print(data)
    return render(request, 'food/statistic.html', {"data": SafeString(data)})
