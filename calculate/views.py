import math

from django.shortcuts import render
from calculate.forms import CalcCaloriesForm
from core.math.Calories import Calories
from core.models import UserExtSettings


def calculate_harrison(request):
    userExt = UserExtSettings.objects.filter(user_id=request.session['user']).order_by('-date_created').first()
    formHarrison = CalcCaloriesForm(request.POST or None, instance=userExt)

    if request.method == 'POST' and formHarrison.is_valid():
        result = Calories.calc_harrison(gender=formHarrison.cleaned_data['gender'],
                                        age=formHarrison.cleaned_data['age'],
                                        weight=formHarrison.cleaned_data['weight'],
                                        height=formHarrison.cleaned_data['height'])
        if formHarrison.cleaned_data['physic_active']:
            result = result * float(request.POST['physic_active'])
    else:
        result = 0
        if userExt:
            result = Calories.calc_harrison(gender=formHarrison.instance.gender,
                                            age=formHarrison.instance.age,
                                            weight=formHarrison.instance.weight,
                                            height=formHarrison.instance.height)

    return render(request, 'calculate/calculate_harrison.html',
                  {"formHarrison": formHarrison, 'resultHarrison': math.ceil(result)})


def calculate_mifflin(request):
    userExt = UserExtSettings.objects.filter(user_id=request.session['user']).order_by('-date_created').first()
    formHarrison = CalcCaloriesForm(request.POST or None, instance=userExt)

    if request.method == 'POST' and formHarrison.is_valid():
        result = Calories.calc_mifflin(gender=formHarrison.cleaned_data['gender'],
                                       age=formHarrison.cleaned_data['age'],
                                       weight=formHarrison.cleaned_data['weight'],
                                       height=formHarrison.cleaned_data['height'])
        if formHarrison.cleaned_data['physic_active']:
            result = result * float(request.POST['physic_active'])
    else:
        result = 0
        if userExt:
            result = Calories.calc_mifflin(gender=formHarrison.instance.gender,
                                           age=formHarrison.instance.age,
                                           weight=formHarrison.instance.weight,
                                           height=formHarrison.instance.height)

    return render(request, 'calculate/calculate_mifflin.html',
                  {"formHarrison": formHarrison, 'resultHarrison': math.ceil(result)})


def calculate_voz(request):
    userExt = UserExtSettings.objects.filter(user_id=request.session['user']).order_by('-date_created').first()
    formHarrison = CalcCaloriesForm(request.POST or None, instance=userExt)

    if request.method == 'POST' and formHarrison.is_valid():

        result = Calories.cacl_voz(age=formHarrison.cleaned_data['age'],
                                   weight=formHarrison.cleaned_data['weight'],
                                   gender=formHarrison.cleaned_data['gender'])
        if formHarrison.cleaned_data['physic_active']:
            result = result * float(request.POST['physic_active'])
    else:
        result = 0
        if userExt:
            result = Calories.cacl_voz(age=formHarrison.instance.age,
                                       weight=formHarrison.instance.weight,
                                       gender=formHarrison.instance.gender)

    return render(request, 'calculate/calculate_voz.html',
                  {"formHarrison": formHarrison, 'resultHarrison': math.ceil(result)})


def calculate_water(request):
    userExt = UserExtSettings.objects.filter(user_id=request.session['user']).order_by('-date_created').first()
    formHarrison = CalcCaloriesForm(request.POST or None, instance=userExt)

    if request.method == 'POST' and formHarrison.is_valid():
        result = Calories.calc_water(weight=formHarrison.cleaned_data['weight'],
                                     gender=formHarrison.cleaned_data['gender'])
    else:
        result = 0
        if userExt:
            result = Calories.calc_water(weight=formHarrison.instance.weight, gender=formHarrison.instance.gender)

    return render(request, 'calculate/calculate_water.html',
                  {"formHarrison": formHarrison, 'resultHarrison': result})
