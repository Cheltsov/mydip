import math
import datetime

from django.db.models import F
from django.shortcuts import render, redirect
from core.models import *


def goal(request):
    if 'user' in request.session:
        goals = Goals.objects.all()
        user_goal = UserGoal.objects.filter(user=request.session['user']).last()
        percent = 0
        countobj = 0
        if user_goal:
            percent = user_goal.goal.bodyworkout_set.filter(
                status=1).count() / user_goal.goal.bodyworkout_set.count() * 100
            countobj = user_goal.goal.bodyworkout_set.count()
        return render(request, 'tracker/goals.html',
                      {'goals': goals, "user_goal": user_goal, "percent": math.ceil(percent), "countobj": countobj})
    else:
        return redirect('auth:auth')


def goal_param(request, id):
    if 'user' in request.session:
        userExt = UserExtSettings.objects.filter(user_id=request.session['user']). \
            values('height', 'weight', 'neck', 'shoulders', 'chest_relax', 'waist', 'left_thigh', 'right_thigh',
                   'left_shin', 'right_shin').order_by('date_created').last()

        bodyParams = NormalBodyParam.objects.get(height=math.ceil(float(userExt['height'])))

        return render(request, 'tracker/goals_plan.html', {'userExt': userExt, 'bodyParams': bodyParams})
    else:
        return redirect('auth:auth')


def select_goal(request, id):
    if 'user' in request.session:
        goalObj = Goals.objects.get(pk=id)
        if goalObj:
            userGoal, created = UserGoal.objects.get_or_create(user_id=request.session['user'], goal=goalObj)
            if created:
                today = datetime.date.today()
                tomorrow = today + datetime.timedelta(days=1)
                for i in range(0, 12):
                    tomorrow = tomorrow + datetime.timedelta(days=2)
                    if tomorrow.today().weekday() == 6:
                        tomorrow = tomorrow + datetime.timedelta(days=1)

                    BodyWorkout.objects.create(title='Тренировка ' + str(i + 1), date_created=tomorrow,
                                               user_id=request.session['user'], goal=goalObj)

                list_work = BodyWorkout.objects.filter(user_id=request.session['user'], goal=goalObj)

                list_ex = [BodyExercise.objects.filter(category='Руки').all(),
                           BodyExercise.objects.filter(category='Ноги').all(),
                           BodyExercise.objects.filter(category='Плечи').all()]

                f = lambda A, n=3: [A[i:i + n] for i in range(0, len(A), n)]
                list3_list_work = f(list_work)
                for listw in list3_list_work:
                    i = 0
                    for item in listw:
                        for item_ex in list_ex[i]:
                            item.publications.add(item_ex.id)
                        item.save()
                        i = i + 1

            return redirect('tracker:workout_list')
    else:
        return redirect('auth:auth')


def workout_list(request):
    if 'user' in request.session:
        list_work = BodyWorkout.objects.filter(user_id=request.session['user']).all()
        return render(request, 'tracker/workout_list.html', {'list_work': list_work})
    else:
        return redirect('auth:auth')


def delete_goal(request, id):
    if 'user' in request.session:
        goalObj = UserGoal.objects.get(goal_id=id)
        goalObj.delete()
        BodyWorkout.objects.filter(goal_id=id).delete()
        return redirect('tracker:goal')
    else:
        return redirect('auth:auth')


def workout_show(request, id):
    if 'user' in request.session:
        objWork = BodyWorkout.objects.get(pk=id)
        return render(request, 'tracker/workout_show.html', {'work': objWork})
    else:
        return redirect('auth:auth')


def workout_stop(request, id):
    if 'user' in request.session:
        objWork = BodyWorkout.objects.get(pk=id)
        objWork.status = 1
        objWork.date_finish = datetime.datetime.now()
        objWork.save()
        return redirect('tracker:workout_show', id=id)
    else:
        return redirect('auth:auth')


def workout_new(request, id):
    if 'user' in request.session:
        list_work = BodyWorkout.objects.filter(id__gte=id)
        for objWork in list_work:
            tomorrow = objWork.date_created.date() + datetime.timedelta(days=1)
            if tomorrow.weekday() == 5:
                tomorrow = tomorrow + datetime.timedelta(days=2)
            elif tomorrow.weekday() == 6:
                tomorrow = tomorrow + datetime.timedelta(days=1)

            objWork.date_created = tomorrow
            objWork.save()

        return redirect('tracker:workout_list')
    else:
        return redirect('auth:auth')
