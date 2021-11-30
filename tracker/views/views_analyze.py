import math
import numpy
from scipy.stats import linregress
import matplotlib.pyplot as plt

from django.shortcuts import render, redirect
from core.models import *


def analyzeIndex(request):
    if 'user' in request.session:
        objExt = UserExtSettings.objects.filter(user_id=request.session['user']).order_by('-date_created').last()

        if not objExt:
            return redirect('tracker:settingsExt')

        listExt = []
        fields = [f for f in objExt._meta.get_fields() if
                  f.name not in ['id', 'user', 'gender', 'age', 'date_created', 'date_updated', 'body_mass_index', 'height', 'weight']]

        for field in fields:
            val = objExt.__getattribute__(field.name)

            listExt.append({
                'key': field.name,
                'value': 0 if val is None else round(val, 2)
            })

        return render(request, 'analyze/index.html', {'listExt': listExt, 'objExt': objExt})
    else:
        return redirect('auth:auth')


def analyzeParam(request, name):
    if 'user' in request.session:

        list_a = UserExtSettings.objects.filter(user_id=request.session['user']).values_list(name, flat=True).order_by(
            'date_created')

        fields = [f for f in UserExtSettings._meta.get_fields() if
                  f.name not in ['id', 'user', 'gender', 'age', 'date_created', 'date_updated', 'body_mass_index', 'height', 'weight']]

        dataReg = []
        for field in fields:
            list_b = UserExtSettings.objects.filter(user_id=request.session['user']).values_list(field.name,
                                                                                                 flat=True).order_by(
                'date_created')

            r = linregress(list(list_a), list(list_b))

            plt.plot(list(list_a), list(list_b), 'ro')
            plt.xlabel(name)
            plt.ylabel(str(field.name))

            plt.title('Fractal dimension with ' + str(r.slope))

            z = numpy.polyfit(list(list_a), list(list_b), 1)
            p = numpy.poly1d(z)
            plt.plot(list(list_a), p(list(list_a)), "b--", )
            plt.savefig('static/analyze/foo_' + str(field.name) + '.png')
            # plt.show()
            plt.close()

            dataReg.append({
                'regression': round(r.slope, 2),
                'image': 'static/analyze/foo_' + str(field.name) + '.png',
                'key': field.name,
                'title': UserExtSettings._meta.get_field(field.name).verbose_name,
                'corr_title': corr_title(round(r.slope, 2))
            })
            print(round(r.slope, 2))
            print(corr_title(round(r.slope, 2)))
            print('---------')

        return render(request, 'analyze/analyze.html',
                      {'dataReg': dataReg, 'current_name': UserExtSettings._meta.get_field(name).verbose_name})
    else:
        return redirect('auth:auth')


def corr_title(reg):
    if reg >= 1:
        return 'Полная положительная корреляция'
    elif 0.8 <= reg < 1:
        return 'Полная положительная корреляция'
    elif 0.6 <= reg < 0.8:
        return 'Сильная положительная корреляция'
    elif 0.05 <= reg < 0.6:
        return 'Умеренная положительная корреляция'
    elif -0.05 < reg < 0.05:
        return 'Никакой корреляции вообще'
    elif -0.6 <= reg < -0.05:
        return 'Умеренная отрицательная корреляция'
    elif -0.8 <= reg < -0.6:
        return 'Сильная положительная корреляция'
    elif -1 <= reg < -0.8:
        return 'Полная отрицательная корреляция'
    elif -1 > reg:
        return 'Полная отрицательная корреляция'
    else:
        return ''