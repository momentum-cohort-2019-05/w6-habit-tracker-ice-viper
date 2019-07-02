from django.shortcuts import render, get_object_or_404, redirect
from core.models import Habit, DailyRecord
from django.contrib.auth.decorators import login_required


# Create your views here.
def welcome_page(request):

    return render(request, 'welcome_page.html', context={})

@login_required
def all_habits(request):
    habits_list = []
    for habit in Habit.objects.filter(user=request.user):
        habits_list.append(habit)

    return render(request, "user_habits.html", {
        'habits_list': habits_list,
        })